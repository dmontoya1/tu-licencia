# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models


class State(models.Model):
    """
    Clase para los departamentos
    """

    code = models.IntegerField("Codigo", null=True, blank=True, unique=True)
    name = models.CharField("Nombre", max_length=50)

    def __str__(self):
        return "%s" % (self.name)


    class Meta:
        verbose_name = "Departamento"


class City(models.Model):
    """
    Clase para los municipios
    """

    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='related_cities',
                              verbose_name="Departamento")
    code = models.CharField("Código", max_length=4, null=True, blank=True)
    name = models.CharField("Nombre", max_length=50)

    def __str__(self):
        return "%s" % (self.name)


    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"


class Police(models.Model):
    """
    clase para las politicas de la plataforma
    """

    TERMINOS_CONDICIONES = 'TC'
    POLITICAS_PRIVACIDAD = 'PP'
    COOKIES = 'CO'

    POLICE_TYPE = (
        (TERMINOS_CONDICIONES, 'Términos y condiciones'),
        (POLITICAS_PRIVACIDAD, 'Políticas de privacidad'),
        (COOKIES, 'Cookies')
    )

    police_type = models.CharField("Tipo de Política", max_length=2, choices=POLICE_TYPE,
                                   unique=True)
    text = models.TextField("Texto")

    def __str__(self):
        return "%s" % (self.police_type)

    class Meta:
        verbose_name = "Politica"
