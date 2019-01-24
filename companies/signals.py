# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import requests
from math import sin, cos, sqrt, atan2, radians

from rest_framework.exceptions import NotFound, APIException

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from .models import Cea, Crc, TransitDepartment, CeaRating, CrcRating, TransitRating

@receiver(post_save, sender=Cea)
def update_address_cea(sender, **kwargs):
    instance = kwargs.get('instance')
    address = instance.address.replace(" ", "+")
    address = address.replace("#", "+")
    url = "https://maps.googleapis.com/maps/api/geocode/json?address={},+{}&key={}".format(
        address, instance.city.name, settings.GOOGLE_MAPS_API_KEY
    )
    result = requests.get(url)
    my_json = result.content.decode('utf8').replace("'", '"')

    data = json.loads(my_json)
    try:
        obj = data['results'][0]['geometry']['location']
    except (KeyError, IndexError):
        print ('Ha ocurrido un error al obtener latitud y longitud')
        # messages.add_message(request, messages.WARNING, ('Ha ocurrido un error al obtener la latitud y la longitud'))
        # raise APIException(detail=("Ha ocurrido un error. Por favor, vuelve a intentarlo"))

    if data['status'] == 'OK':
        print (obj)
        if instance.lat == None or instance.lon == None:
            instance.lat = obj['lat']
            instance.lon = obj['lng']
            instance.save()

@receiver(post_save, sender=Crc)
def update_address_crc(sender, **kwargs):

    instance = kwargs.get('instance')
    address = instance.address.replace(" ", "+")
    address = address.replace("#", "+")
    url = "https://maps.googleapis.com/maps/api/geocode/json?address={},+{}&key={}".format(
        address, instance.city.name, settings.GOOGLE_MAPS_API_KEY
    )
    print (url)
    result = requests.get(url)
    print (result.content)
    print (type(result.content))
    response = json.loads(result.content)
    try:
        obj = response['results'][0]['geometry']['location']
    except (KeyError, IndexError):
        print ('Ha ocurrido un error al obtener latitud y longitud')
        # messages.add_message(request, messages.WARNING, ('Ha ocurrido un error al obtener la latitud y la longitud'))
        # raise APIException(detail=("Ha ocurrido un error. Por favor, vuelve a intentarlo"))

    if response['status'] == 'OK':
        if instance.lat == None or instance.lon == None:
            instance.lat = obj['lat']
            instance.lon = obj['lng']
            instance.save()

@receiver(post_save, sender=TransitDepartment)
def update_address_transit(sender, **kwargs):
    instance = kwargs.get('instance')
    address = instance.address.replace(" ", "+")
    address = address.replace("#", "+")
    url = "https://maps.googleapis.com/maps/api/geocode/json?address={},+{}&key={}".format(
        address, instance.city.name, settings.GOOGLE_MAPS_API_KEY
    )
    print (url)
    result = requests.get(url)
    response = json.loads(result.content)
    try:
        obj = response['results'][0]['geometry']['location']
    except (KeyError, IndexError):
        print ('Ha ocurrido un error al obtener latitud y longitud')
        # messages.add_message(request, messages.WARNING, ('Ha ocurrido un error al obtener la latitud y la longitud'))
        # raise APIException(detail=("Ha ocurrido un error. Por favor, vuelve a intentarlo"))

    if response['status'] == 'OK':
        if instance.lat == None or instance.lon == None:
            instance.lat = obj['lat']
            instance.lon = obj['lng']
            instance.save()

@receiver(post_save, sender=CeaRating)
def update_rating_cea(sender, **kwargs):
    if kwargs.get('created') is True:
        instance = kwargs.get('instance')
        cea = instance.cea
        ratings = CeaRating.objects.filter(cea=cea).aggregate(Avg('stars'))
        if ratings['stars__avg']:
            cea.rating = ratings['stars__avg']
            cea.save()
        
@receiver(post_save, sender=CrcRating)
def update_rating_crc(sender, **kwargs):
    if kwargs.get('created') is True:
        instance = kwargs.get('instance')
        crc = instance.crc
        ratings = CrcRating.objects.filter(crc=crc).aggregate(Avg('stars'))
        if ratings['stars__avg']:
            crc.rating = ratings['stars__avg']
            crc.save()
        
@receiver(post_save, sender=TransitRating)
def update_rating_transit(sender, **kwargs):
    if kwargs.get('created') is True:
        instance = kwargs.get('instance')
        transit = instance.transit
        ratings = TransitRating.objects.filter(transit=transit).aggregate(Avg('stars'))
        if ratings['stars__avg']:
            transit.rating = ratings['stars__avg']
            transit.save()
