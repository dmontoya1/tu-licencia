
from django.conf import settings
from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.views import sendEmail
from manager.models import City

from .serializers import CeaSerializer, CrcSerializer, TransitSerializer, CeaDetailSerializer, CrcDetailSerializer
from .models import Crc, Cea, TransitDepartment
from .utils import params_to_filter


class CrcList(generics.ListAPIView):
    """
    """

    serializer_class = CrcSerializer

    def get_queryset(self):
        get_list = self.request.GET.copy()
        get_list.pop('age')
        get_list.pop('gender')
        get_list.pop('licences')
        try:
            rating = get_list['rating']
            get_list.pop('rating')
        except:
            rating = None
        try:
            price = get_list['price']
            get_list.pop('price')
        except:
            price = None

        params = params_to_filter(get_list.items())
        query = Crc.objects.filter(**params).distinct()
        try:
            if rating:
                if rating == "1":
                    if price:
                        if price == "1":
                            query = query.order_by('rating', 'price')
                        elif price == "2":
                            query = query.order_by('rating', '-price')
                        else:
                            query = query.order_by('rating')
                    else:
                        query = query.order_by('rating')
                elif rating == "2":
                    if price:
                        if price == "1":
                            query = query.order_by('-rating', 'price')
                        elif price == "2":
                            query = query.order_by('-rating', '-price')
                        else:
                            query = query.order_by('-rating')
                    else:
                        query = query.order_by('-rating')
            elif price:
                if price == "1":
                    query = query.order_by('price')
                elif price == "2":
                    query = query.order_by('-price')
        except Exception as e:
            print (e)
        return query


class CeaList(generics.ListAPIView):
    """
    """

    serializer_class = CeaSerializer
    
    def get_queryset(self):
        get_list = self.request.GET.copy()
        get_list.pop('age')
        get_list.pop('gender')
        get_list.pop('licences')
        try:
            rating = get_list['rating']
            get_list.pop('rating')
        except:
            rating = None
        try:
            price = get_list['price']
            get_list.pop('price')
        except:
            price = None
        params = params_to_filter(get_list.items())
        query = Cea.objects.filter(**params).distinct()
        try:
            if rating:
                if rating == "1":
                    if price:
                        if price == "1":
                            query = query.order_by('rating', 'final_price')
                        elif price == "2":
                            query = query.order_by('rating', '-final_price')
                        else:
                            query = query.order_by('rating')
                    else:
                        query = query.order_by('rating')
                elif rating == "2":
                    if price:
                        if price == "1":
                            query = query.order_by('-rating', 'final_price')
                        elif price == "2":
                            query = query.order_by('-rating', '-final_price')
                        else:
                            query = query.order_by('-rating')
                    else:
                        query = query.order_by('-rating')
            elif price:
                if price == "1":
                    query = query.order_by('final_price')
                elif price == "2":
                    query = query.order_by('-final_price')
        except Exception as e:
            print (e)
        return query


class CeaCityList(generics.ListAPIView):
    """
    """

    serializer_class = CrcDetailSerializer
    
    def get_queryset(self):
        city = City.objects.get(id=self.request.GET.get('city')) 
        query = Cea.objects.filter(city=city).distinct()
        return query


class CrcCityList(generics.ListAPIView):
    """
    """

    serializer_class = CrcDetailSerializer
    
    def get_queryset(self):
        city = City.objects.get(id=self.request.GET.get('city')) 
        query = Crc.objects.filter(city=city).distinct()
        return query


class TransitList(generics.ListAPIView):
    """
    """

    serializer_class = TransitSerializer

    def get_queryset(self):
        get_list = self.request.GET.copy()
        try:
            rating = get_list['rating']
            get_list.pop('rating')
        except:
            rating = None
        try:
            price = get_list['price']
            get_list.pop('price')
        except:
            price = None
        params = params_to_filter(get_list.items())
        query = TransitDepartment.objects.filter(**params).distinct()
        try:
            if rating:
                if rating == "1":
                    if price:
                        if price == "1":
                            query = query.order_by('rating', 'price')
                        elif price == "2":
                            query = query.order_by('rating', '-price')
                        else:
                            query = query.order_by('rating')
                    else:
                        query = query.order_by('rating')
                elif rating == "2":
                    if price:
                        if price == "1":
                            query = query.order_by('-rating', 'price')
                        elif price == "2":
                            query = query.order_by('-rating', '-price')
                        else:
                            query = query.order_by('-rating')
                    else:
                        query = query.order_by('-rating')
            elif price:
                if price == "1":
                    query = query.order_by('price')
                elif price == "2":
                    query = query.order_by('-price')
        except Exception as e:
            print (e)
        return query


class DisableCrcRequest(APIView):
    """
    """

    def post(self, request):
        try:
            nit = request.data['nit']
            crc = Crc.objects.get(nit=nit)
            url = 'http://{}/admin/companies/crc/{}/change/'.format(request.get_host(), crc.pk)
            ctx = {
            'title': 'Solicitud de inactivación CRC',
            'content': 'El CRC {} ha solicitado inactivar su companía. Para verlo has click en el siguiente botón'.format(crc.name),
            'url': url 
            }

            sendEmail(ctx, settings.EMAIL_ADMIN, 'Solicitud Inhabilitación')
            message = 'Se ha enviado la solicitud con éxito'
            response = {'detail': message}
            status_e = status.HTTP_201_CREATED

        except Exception as e:
            print (e)
            message = 'Ha ocurrido un error inesperado'
            response = {'error': message}
            status_e = status.HTTP_400_BAD_REQUEST

        return Response(response, status=status_e)


class DisableCeaRequest(APIView):
    """
    """

    def post(self, request):
        try:
            nit = request.data['nit']
            cea = Cea.objects.get(nit=nit)
            url = 'http://{}/admin/companies/cea/{}/change/'.format(request.get_host(), cea.pk)
            ctx = {
            'title': 'Solicitud de inactivación CEA',
            'content': 'El CEA {} ha solicitado inactivar su companía. Para verlo has click en el siguiente botón'.format(cea.name),
            'url': url 
            }

            sendEmail(ctx, settings.EMAIL_ADMIN, 'Solicitud Inhabilitación')
            message = 'Se ha enviado la solicitud con éxito'
            response = {'detail': message}
            status_e = status.HTTP_201_CREATED

        except Exception as e:
            print (e)
            message = 'Ha ocurrido un error inesperado'
            response = {'error': message}
            status_e = status.HTTP_400_BAD_REQUEST

        return Response(response, status=status_e)


class EnableCrcRequest(APIView):
    """
    """

    def post(self, request):
        try:
            nit = request.data['nit']
            crc = Crc.objects.get(nit=nit)
            url = 'http://{}/admin/companies/crc/{}/change/'.format(request.get_host(), crc.pk)
            ctx = {
            'title': 'Solicitud de activación CRC',
            'content': 'El CRC {} ha solicitado activar su companía. Para verlo has click en el siguiente botón'.format(crc.name),
            'url': url 
            }

            sendEmail(ctx, settings.EMAIL_ADMIN, 'Solicitud Habilitación')
            message = 'Se ha enviado la solicitud con éxito'
            response = {'detail': message}
            status_e = status.HTTP_201_CREATED

        except Exception as e:
            print (e)
            message = 'Ha ocurrido un error inesperado'
            response = {'error': message}
            status_e = status.HTTP_400_BAD_REQUEST

        return Response(response, status=status_e)


class EnableCeaRequest(APIView):
    """
    """

    def post(self, request):
        try:
            nit = request.data['nit']
            cea = Cea.objects.get(nit=nit)
            url = 'http://{}/admin/companies/cea/{}/change/'.format(request.get_host(), cea.pk)
            ctx = {
            'title': 'Solicitud de activación CEA',
            'content': 'El CEA {} ha solicitado activar su companía. Para verlo has click en el siguiente botón'.format(cea.name),
            'url': url 
            }

            sendEmail(ctx, settings.EMAIL_ADMIN, 'Solicitud habilitación')
            message = 'Se ha enviado la solicitud con éxito'
            response = {'detail': message}
            status_e = status.HTTP_201_CREATED

        except Exception as e:
            print (e)
            message = 'Ha ocurrido un error inesperado'
            response = {'error': message}
            status_e = status.HTTP_400_BAD_REQUEST

        return Response(response, status=status_e)

