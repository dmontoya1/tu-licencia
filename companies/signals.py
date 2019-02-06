# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json
import requests

from rest_framework.exceptions import NotFound, APIException

from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from .models import CeaRating, CrcRating, TransitRating


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
