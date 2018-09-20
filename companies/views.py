from django.shortcuts import render

from rest_framework import generics

from .serializers import CeaLicenceSerializer
from .models import Crc, Cea, TransitDepartment


class CeaList(generics.ListAPIView):
    """
    """

    serializer_class = CeaLicenceSerializer
    queryset = Cea.objects.all()
