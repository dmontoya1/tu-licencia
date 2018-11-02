
from django.db.models import Q
from django.shortcuts import render

from rest_framework import generics

from companies.utils import params_to_filter
from .models import Vehicle
from .serializers import VehicleSerializer


class VehicleList(generics.ListAPIView):
    """ Lista todos los vehículos disponibles 
    """

    serializer_class = VehicleSerializer

    def get_queryset(self):
        get_list = self.request.GET.copy()
        params = params_to_filter(get_list.items())
        licence_1 = Q(licences__category=params['licences'][0])
        if params['licences'][1] != '':
            licence_2 = Q(licences__category=params['licences'][1])
            return Vehicle.objects.filter(licence_1 | licence_2 & Q(deleted_at=None))
        return Vehicle.objects.filter(licence_1 & Q(deleted_at=None))
