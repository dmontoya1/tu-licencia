from datetime import datetime

from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import render

from companies.models import Cea, Crc, TransitDepartment
from licences.models import Licence
from manager.models import State, City
from users.models import User
from .models import Request
from .serializers import RequestSerializer


class RequestCreate(APIView):
    """
    """

    def post(self, request):
        try:
            user_data = request.data['user']
            cea = Cea.objects.get(pk=request.data['cea'])
            crc = Crc.objects.get(pk=request.data['crc'])
            transit = TransitDepartment.objects.get(pk=request.data['transit'])
            crc_price = request.data['crc_price']
            cea_price = request.data['cea_price']
            transit_price = request.data['transit_price']

            city = City.objects.get(pk=user_data['city'])
            state = city.state
            try:
                user = User.objects.get(username=user_data['document_id'])
            except User.DoesNotExist:
                birth_date = datetime.strptime(user_data['birth_date'], '%m-%d-%Y')
                user = get_user_model()
                user = user()
                user.username = user_data['document_id']
                user.email = user_data['email']
                user.set_password(user_data['password'])
                user.first_name = user_data['first_name']
                user.last_name = user_data['last_name']
                user.cellphone = user_data['cellphone']
                user.user_type = User.CLIENTE
                user.document_type = User.CEDULA_CIUDADANIA
                user.document_id = user_data['document_id']
                user.state = state
                user.city = city
                user.gender = user_data['gender']
                user.birth_date = birth_date
                user.backend = 'django.contrib.auth.backends.ModelBackend'
                user.save()
                Token.objects.create(user=user)

            if (request.data['runt'] == 'si'):
                runt = True
            else:
                runt = False
            
            total_price = int(crc_price) + int(cea_price) + int(transit_price)

            request_obj = Request(
                user=user,
                cea=cea,
                crc=crc,
                transit=transit,
                payment_type = request.data['payment_type'],
                has_runt=runt,
                total_price=total_price
            )
            request_obj.save()

            for i in range(0, len(request.data['licences'])):
                licence = Licence.objects.get(category=request.data['licences'][i])
                request_obj.licences.add(licence)
            
            request_obj.save()
            message = 'Se ha creado la solicitud con éxito'
            response = {'detail': message, 'request': request_obj.pk}
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

