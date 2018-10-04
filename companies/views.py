from django.shortcuts import render

from rest_framework import generics

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
        params = params_to_filter(self.request.GET.items())
        return Cea.objects.filter(**params).distinct()


class TransitList(generics.ListAPIView):
    """
    """

    serializer_class = TransitSerializer

    def get_queryset(self):
        params = params_to_filter(self.request.GET.items())
        return TransitDepartment.objects.filter(**params).distinct()
