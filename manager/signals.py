# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
from django.db.models import Avg
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings

from core.views import sendEmail

from .models import ContactForm

@receiver(post_save, sender=ContactForm)
def send_contact_form_mail(sender, **kwargs):
    if kwargs.get('created') is True:
        instance = kwargs.get('instance')
        current_site = Site.objects.get_current()
        url = 'http://{}/admin/manager/contactform/{}/change/'.format(current_site.domain, instance.pk)
        ctx = {
            'title': 'Nuevo formulario de contacto',
            'content': 'Se ha creado un nuevo formulario de contacto. Para ingresar sigue el siguiente link:',
            'url': url,
            'action': 'Ver formulario'
        }

        sendEmail(ctx, settings.EMAIL_ADMIN, 'Nuevo formulario de contacto')
