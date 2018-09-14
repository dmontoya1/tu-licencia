# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.contrib.auth.models import AbstractUser
from django.contrib.sessions.models import Session
from django.core.exceptions import ValidationError
from django.db import models

from manager.models import City, State


class User(AbstractUser):
    """
    Clase para manejar todos los usuarios de la plataforma
    """

    CEDULA_CIUDADANIA = 'CC'
    CEDULA_EXTRANJERA = 'CE'
    TARJETA_IDENTIDAD = 'TI'
    MANAGER = 'MAN'
    CLIENTE = 'CLI'
    EXPRESS_USER = 'EXU'
    DOCUMENT_TYPE = (
        (CEDULA_CIUDADANIA, 'Cédula de ciudadania'),
        (CEDULA_EXTRANJERA, 'Cédula de extranjería'),
        (TARJETA_IDENTIDAD, 'Tarjeta de identidad'),
    )
    USER_TYPE = (
        (MANAGER, 'Administrador de CEA o CRC'),
        (CLIENTE, 'Cliente'),
        (EXPRESS_USER, 'Usuario express')
    )

    email = models.EmailField("Email", unique=False)
    password = models.CharField(
        "Password",
        max_length=128,
        blank=True,
        null=True
    )
    user_type = models.CharField(
        "Tipo Usuario",
        max_length=3,
        choices=USER_TYPE
    )
    document_type = models.CharField(
        "Tipo Documento",
        max_length=3,
        choices=DOCUMENT_TYPE
    )
    document_id = models.CharField(
        "Número Documento",
        max_length=15,
        unique=False
    )
    phone_number = models.CharField(
        "Telefono",
        max_length=15,
        blank=True,
        null=True
    )
    cellphone = models.CharField("Celular", max_length=10)
    city = models.ForeignKey(
        City,
        verbose_name="Ciudad",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    state = models.ForeignKey(
        State,
        verbose_name="Departamento",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    address = models.CharField(
        "Dirección",
        max_length=255,
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        return "%s %s (%s)" % (self.first_name, self.last_name, self.document_id)
