# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import sys
import json
from math import sin, cos, sqrt, atan2, radians
from datetime import datetime, timedelta
from math import sin, cos, sqrt, atan2, radians
from django.conf import settings
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse
from rest_framework import generics
from rest_framework.exceptions import APIException
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

import requests


from .models import Police, State, City, Sector
from .serializers import PoliceSerializer, StateSerializer, CitySerializer, SectorSerializer,\
                         ContactFormSerializer


class TermsAndConditions(generics.ListAPIView):
    """
    Api para obtener terminos y condiciones
    """
    queryset = Police.objects.filter(police_type='TC')
    serializer_class = PoliceSerializer


class PrivacyPolicies(generics.ListAPIView):
    """
    Api para obtener politicas de privacidad
    """
    queryset = Police.objects.filter(police_type='PP')
    serializer_class = PoliceSerializer


class StateList(generics.ListAPIView):
    """
    Api para obtener los departamentos
    """
    permission_classes = (AllowAny,)
    queryset = State.objects.alive().order_by('name')
    serializer_class = StateSerializer


class CityList(generics.ListAPIView):
    """
    Api para obtener los municipios dependiendo del departamento
    """

    permission_classes = (AllowAny,)
    serializer_class = CitySerializer

    def get_queryset(self):
        queryset = City.objects.alive()
        stateId = self.kwargs['stateId']
        if stateId:
            queryset = queryset.filter(state=stateId).order_by('name')
        return queryset


class SectorList(generics.ListAPIView):
    """
    Api para obtener los sectores dependiendo del municipio
    """

    permission_classes = (AllowAny,)
    serializer_class = SectorSerializer

    def get_queryset(self):
        queryset = Sector.objects.alive()
        cityId = self.kwargs['cityId']
        if cityId:
            queryset = queryset.filter(city=cityId).order_by('name')
        return queryset


class ContactForm(generics.CreateAPIView):
    """Vista para crear las peticiones que se envían en los formularios de contacto
    """

    permission_classes = (AllowAny,)
    serializer_class = ContactFormSerializer
