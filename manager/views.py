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

from manager.models import City, Location
from schools.models import Student, Level
from users.models import User
from .models import Police, State, City, Location, Notification
from .serializers import PoliceSerializer, StateSerializer, CitySerializer, LocationSerializer,\
                         NotificationListSerializer


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
    queryset = State.objects.all()
    serializer_class = StateSerializer


class CityList(generics.ListAPIView):
    """
    Api para obtener los municipios dependiendo del departamento
    """

    serializer_class = CitySerializer

    def get_queryset(self):
        queryset = City.objects.all()
        stateId = self.kwargs['stateId']
        if stateId:
            queryset = queryset.filter(state=stateId)
        return queryset


class GetLocation(generics.GenericAPIView):
    """
    Función para obtener la cercania entre 2 latitudes y longitudes
    Si la lat y lon estan a 10 mts de cercanía de un punto que ya existe
    retorna ese punto. Sino, crea uno nuevo y lo retorna
    """
    serializer_class = LocationSerializer
    permission_classes = (AllowAny,)

    def post(self, request, format=None):
        lat1 = float(request.POST['lat'])
        lon1 = float(request.POST['lon'])
        radius = 6371 * 1000 #Aproximadamente el radio de la tierra en metros
        latitude1 = radians(lat1)
        longitude1 = radians(lon1)

        locations = Location.objects.all()

        for location in locations:
            lat2 = radians(location.latitude)
            lon2 = radians(location.longitude)

            dlon = lon2 - longitude1
            dlat = lat2 - latitude1

            a = sin(dlat / 2)**2 + cos(latitude1) * cos(lat2) * sin(dlon / 2)**2
            c = 2 * atan2(sqrt(a), sqrt(1 - a))
            distance = radius * c

            if distance < 10:
                location.is_new = False
                location.save()
                serializer = LocationSerializer(location, many=False)
                return Response(serializer.data)

        location = Location(
            latitude=lat1,
            longitude=lon1,
            is_new=True,
        )
        location.save()
        serializer = LocationSerializer(location)
        return Response(serializer.data)


class NotificationHistoryList(generics.ListAPIView):
    """
    Api para generar el historial de notificaciones de conductor o acudiente
    Recibe el Authorization Token
    """

    serializer_class = NotificationListSerializer

    def get_queryset(self):
        user = self.request.auth.user
        last_5_days = datetime.today() - timedelta(days=5)
        if user:
            user_notifications = Q(user=user)
            general_notifications = Q(user=None)
            last_days = Q(date__gte=last_5_days)
            queryset = Notification.objects.filter((user_notifications | general_notifications) & last_days).order_by('-date')
        else:
            queryset = Notification.objects.all()
        return queryset


class UpdateLocation(generics.UpdateAPIView):
    """
    Api para actualizar la localización de recogida del alumno
    de una ruta
    """
    serializer_class = LocationSerializer
    queryset = Location.objects.all()


def process_xlsx(request):

    if request.method == "GET":
        return HttpResponseRedirect(reverse("admin:index"))
    else:
        try:
            student_count = 0
            records = request.FILES['file'].get_records()
            user = request.user
            if user.user_type != User.COORDINADOR:
                messages.error(request,'Debes ser coordinador para cargar un archivo CSV')
                return HttpResponseRedirect(reverse("admin:index"))
            else:
                with transaction.atomic():
                    for record in records:
                        try:
                            student = Student.objects.get(document_id=record['NumeroDocumento'])
                            messages.error(request, 'Ya existe un estudiante con documento \
                            '+ str(record['NumeroDocumento']) + '')
                            return HttpResponseRedirect('/admin/schools/student/?q=' + str(record['NumeroDocumento']) + '')
                        except:
                            pass
                        try:
                            level = Level.objects.get(
                                name=record['Grado'],
                                calendar=record['Calendario'],
                                school=user.school)
                        except Level.DoesNotExist:
                            messages.error(request, 'No se ha encontrado el grado para el estudiante con documento \
                            '+ str(record['NumeroDocumento']) + '')
                            return HttpResponseRedirect(reverse("admin:index"))
                        try:
                            city = City.objects.get(name=record['Ciudad'])
                        except City.DoesNotExist:
                            messages.error(request, 'No se ha encontrado la ciudad para el estudiante con documento \
                            '+ str(record['NumeroDocumento']) + '')
                            return HttpResponseRedirect(reverse("admin:index"))
                        
                        address = record['Direccion'].replace(" ", "+")
                        url = "https://maps.googleapis.com/maps/api/geocode/json?address={},+{}&key={}".format(
                            address, city.name, settings.GOOGLE_MAPS_API_KEY
                        )
                        result = requests.get(url)
                        response = json.loads(result.content)
                        try:
                            obj = response['results'][0]['geometry']['location']
                        except (KeyError, IndexError):
                            raise APIException(detail=("Ha ocurrido un error. Por favor, vuelve a intentarlo"))

                        if response['status'] == 'OK':
                            lat1 = float(obj['lat'])
                            lon1 = float(obj['lng'])
                            radius = 6371 * 1000 #Aproximadamente el radio de la tierra en metros
                            latitude1 = radians(lat1)
                            longitude1 = radians(lon1)

                            locations = Location.objects.all()

                            for location in locations:
                                lat2 = radians(location.latitude)
                                lon2 = radians(location.longitude)

                                dlon = lon2 - longitude1
                                dlat = lat2 - latitude1

                                a = sin(dlat / 2)**2 + cos(latitude1) * cos(lat2) * sin(dlon / 2)**2
                                c = 2 * atan2(sqrt(a), sqrt(1 - a))
                                distance = radius * c

                                if distance < 10:
                                    location.is_new = False
                                    location.save()
                                    student_location = location
                                    break
                            else:
                                location = Location(
                                    latitude=lat1,
                                    longitude=lon1,
                                    is_new=True,
                                )
                                location.save()
                                student_location = location
                        else:
                            messages.error(request, 'No se ha encontrado la dirección {} del alumno {} {} en los mapas'.format(
                                record['Direccion'], record['Nombres'], record['Apellidos']))
                            return HttpResponseRedirect(reverse("admin:index"))

                        student = Student(
                            first_name=record['Nombres'],
                            last_name=record['Apellidos'],
                            document_type=record['TipoDocumento'],
                            document_id=record['NumeroDocumento'],
                            city=city,
                            address=record['Direccion'],
                            address_complements=record['Complementos'],
                            neighborhood=record['Barrio'],
                            calendar=record['Calendario'],
                            level=level,
                            school=user.school,
                            location=student_location,
                        )
                        student.save()
                        student_count += 1

                messages.success(request, 'La importación de los alumnos ha sido exitosa. Se han registrado ' + str(student_count) + ' alumnos')
                return HttpResponseRedirect('/admin/schools/student/')

        except (KeyError, ObjectDoesNotExist), e:
            messages.error(request,'El archivo no cumple con los parámetros de integridad requeridos, faltan campos obligatorios. (Ver Factores a tener en cuenta)' )
        except Exception, e:
            messages.error(request, 'Ha ocurrido un error inesperado' )
            messages.error(request, '{} @ {}:{}'.format(e.message, sys.exc_info()[2].tb_frame.f_code.co_filename, sys.exc_info()[2].tb_lineno))

        return HttpResponseRedirect(reverse("admin:index"))
