
from django.conf import settings
from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from core.views import sendEmail

from .serializers import CeaSerializer, CrcSerializer, TransitSerializer
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
        params = params_to_filter(get_list.items())
        return Crc.objects.filter(**params).distinct()


class CeaList(generics.ListAPIView):
    """
    """

    serializer_class = CeaSerializer
    
    def get_queryset(self):
        get_list = self.request.GET.copy()
        get_list.pop('age')
        get_list.pop('gender')
        get_list.pop('licences')
        params = params_to_filter(get_list.items())
        return Cea.objects.filter(**params).distinct()


class TransitList(generics.ListAPIView):
    """
    """

    serializer_class = TransitSerializer

    def get_queryset(self):
        params = params_to_filter(self.request.GET.items())
        return TransitDepartment.objects.filter(**params).distinct()


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

