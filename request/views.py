from datetime import datetime

from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from django.conf import settings
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render, reverse

from core.views import sendEmail, sendBaucherEmail
from companies.models import Cea, Crc, TransitDepartment
from licences.models import Licence
from manager.models import State, City
from users.models import User
from .models import Request, RequestTramit
from .serializers import RequestSerializer


class RequestCreate(APIView):
    """
    """

    def post(self, request):
        try:
            user_data = request.data['user']
            cea = Cea.objects.get(pk=request.data['cea'])
            try:
                crc = Crc.objects.get(pk=request.data['crc'])
            except:
                crc = None
            transit = TransitDepartment.objects.get(pk=request.data['transit'])
            crc_price = request.data['crc_price']
            cea_price = request.data['cea_price']
            transit_price = request.data['transit_price']
            tramits = request.data['tramits']
            city = City.objects.get(pk=user_data['city'])
            state = State.objects.get(pk=user_data['state'])
            # state = city.state
            try:
                user = User.objects.get(username=user_data['document_id'])
                token, created = Token.objects.get_or_create(user=user)
            except User.DoesNotExist:
                print (user_data)
                birth_date = datetime.strptime(user_data['birth_date'], '%m/%d/%Y')
                user = get_user_model()
                user = user()
                user.username = user_data['document_id']
                user.email = user_data['email']
                try:
                    user.set_password(user_data['password'])
                except:
                    print ('Not password supply')
                user.first_name = user_data['first_name']
                user.last_name = user_data['last_name']
                user.cellphone = user_data['cellphone']
                user.phone_number = user_data['phone_number']
                user.address = user_data['address']
                user.user_type = User.CLIENTE
                user.document_type = user_data['document_type']
                user.document_id = user_data['document_id']
                user.state = state
                user.city = city
                user.gender = user_data['gender']
                user.birth_date = birth_date
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                user.save()
                token = Token.objects.create(user=user)

            if (request.data['runt'] == 'si'):
                runt = True
            else:
                runt = False
            
            total_price = int(crc_price) + int(cea_price) + int(transit_price)

            try:
                if request.user.user_type == User.EXPRESS_USER:
                    user_request = request.user
                else:
                    user_request = None
            except:
                user_request = None

            request_obj = Request(
                user=user,
                user_request=user_request,
                cea=cea,
                crc=crc,
                transit=transit,
                payment_type = request.data['payment_type'],
                payment_value = request.data['payment_value'],
                payment_type2 = request.data['payment_type2'],
                payment_value2 = request.data['payment_value2'],
                has_runt=runt,
                total_price=total_price,
                credit_status=Request.PENDIENTE_APROBACION,
                state=user.state,
                paper=request.data['paper']
            )
            request_obj.save()
            
            licence1 = tramits['licence_1']
            licence2 = tramits['licence_2']

            tramit1 = RequestTramit(
                request=request_obj,
                tramit_type=licence1['tramit'],
                licence=Licence.objects.get(category=licence1['licence'])
            )
            tramit1.save()
            if (licence2 != ''):
                tramit2 = RequestTramit(
                    request=request_obj,
                    tramit_type=licence2['tramit'],
                    licence=Licence.objects.get(category=licence2['licence'])
                )
                tramit2.save()
            # ctx = {
            #     "title": "Instrucciones para sacar tu licencia",
            #     "content": "Hola. a continuación están las instrucciones para que puedas sacar tu licencia",
            #     "url": reverse('webclient:login'),
            #     "action": "Ver mi perfil"
            # }
            # params = {
            #     'request':request_obj
            # }

            # sendBaucherEmail(ctx, request_obj.user.email, 'Instrucciones TuLicencia', params=params)

            message = 'Se ha creado la solicitud con éxito'
            response = {'detail': message, 'request': request_obj.pk, 'booking': request_obj.booking}
            status_e = status.HTTP_201_CREATED
        except Exception as e:
            print (e)
            message = 'Ha ocurrido un error inesperado'
            response = {'error': message}
            status_e = status.HTTP_400_BAD_REQUEST

        return Response(response, status=status_e)


class ValidRequestDocument(APIView):
    """
    """

    def get(self, request):
        try:
            booking = request.GET['booking']
            document = request.GET['document']

            request_obj = Request.objects.get(booking=booking)
            if request_obj:
                if request_obj.user.document_id == document:
                    response = {'detail': 'Los usuarios son iguales'}
                    status_e = status.HTTP_200_OK
                else:
                    response = {'error': 'Los documentos no coinciden'}
                    status_e = status.HTTP_400_BAD_REQUEST
        except Exception as e:
            print (e)
            message = 'Ha ocurrido un error inesperado'
            response = {'error': message}
            status_e = status.HTTP_400_BAD_REQUEST

        return Response(response, status=status_e)


class CRCPendingRequestList(generics.ListAPIView):
    """
    """

    serializer_class = RequestSerializer

    def get_queryset(self):
        nit = self.request.GET['nit']
        crc = Crc.objects.get(nit=nit)

        requests = Request.objects.filter(crc=crc, crc_status=Request.HAS_NOT_STARTER)
        return requests


class CEAPendingRequestList(generics.ListAPIView):
    """
    """

    serializer_class = RequestSerializer

    def get_queryset(self):
        nit = self.request.GET['nit']
        cea = Cea.objects.get(nit=nit)

        requests = Request.objects.filter(cea=cea, cea_status=Request.HAS_NOT_STARTER)
        return requests


class CancelRequest(APIView):
    """Api para hacer la solicitud de cancelacion de
    la solicitud de un usuario
    """

    def post(self, request):
        pk = self.request.data.get('pk')
        request_obj = Request.objects.get(pk=pk)

        request_obj.request_status = Request.CANCEL
        request_obj.save()

        url = 'http://{}/admin/request/request/{}/change/'.format(request.get_host(), request_obj.pk)

        ctx = {
            'title': 'Solicitud de cancelacion de servicio',
            'content': 'El usuario {} con correo {} ha solicitado la cancelacion de su servicio. Para verlo has click en el siguiente botón'.format(request_obj.user.get_full_name(), request_obj.user.email),
            'url': url,
            'action': 'Ver solicitud'
        }

        sendEmail(ctx, settings.EMAIL_ADMIN, 'Solicitud cancelación servicio')

        return Response("Cancelación realizada con éxito", status.HTTP_200_OK)
