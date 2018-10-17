# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.contrib.auth.models import AbstractUser
from django.contrib.sessions.models import Session
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from manager.models import City, State
from utils.managers import SoftDeletionManager


class User(AbstractUser):
    """
    Clase para manejar todos los usuarios de la plataforma
    """

    CEDULA_CIUDADANIA = 'CC'
    CEDULA_EXTRANJERA = 'CE'
    TARJETA_IDENTIDAD = 'TI'
    ADMIN_CEA = 'CEA'
    ADMIN_CRC = 'CRC'
    CLIENTE = 'CLI'
    EXPRESS_USER = 'EXU'

    MASCULINO = 'M'
    FEMENINO = 'F'

    DOCUMENT_TYPE = (
        (CEDULA_CIUDADANIA, 'Cédula de ciudadania'),
        (CEDULA_EXTRANJERA, 'Cédula de extranjería'),
        (TARJETA_IDENTIDAD, 'Tarjeta de identidad'),
    )
    USER_TYPE = (
        (ADMIN_CEA, 'Administrador de CEA'),
        (ADMIN_CRC, 'Administrador de CRC'),
        (CLIENTE, 'Cliente'),
        (EXPRESS_USER, 'Usuario express')
    )

    GENDER = (
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
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
    state = models.ForeignKey(
        State,
        verbose_name="Departamento",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    city = models.ForeignKey(
        City,
        verbose_name="Ciudad",
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
    gender = models.CharField(
        "Género",
        max_length=2,
        choices=GENDER,
        blank=True, null=True
    )
    birth_date = models.DateField(
        "Fecha de Nacimiento",
        blank=True, null=True
    )
    deleted_at = models.DateTimeField(blank=True, null=True)
    # objects = SoftDeletionManager()


    class Meta:
        verbose_name = "Usuario"
        verbose_name_plural = "Usuarios"

    def __str__(self):
        if self.user_type == self.CLIENTE:
            return "%s %s" %(self.first_name, self.last_name)
        return "%s %s (%s)" % (self.first_name, self.last_name, self.document_id)


    def soft_delete(self):
        """Ejecuta un borrado lógico desde la instancia
        """

        self.deleted_at = timezone.now()
        self.save()

    def revive(self):
        """Habilita un objeto que esté lógicamente borrado
        """

        self.deleted_at = None
        self.save()
