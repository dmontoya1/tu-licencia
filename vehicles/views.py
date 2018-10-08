from django.shortcuts import render

from rest_framework import generics

from .models import Vehicle
from .serializers import VehicleSerializer


class VehicleList(generics.ListAPIView):
    """ Lista todos los vehículos disponibles 
    """

    serializer_class = VehicleSerializer
    queryset = Vehicle.objects.alive()

