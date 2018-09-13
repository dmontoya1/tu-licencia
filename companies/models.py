# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError
from django.db import models

from licences.models import Licence
from manager.models import State, City
from vehicles.models import Vehicle
from .utils import get_upload_to


class Cea(models.Model):
    """Modelo para guardar los datos de los cea
    Centro de Enseñanaza Automovilísitico
    """

    MEDIA_PATH = 'cea'

    name = models.CharField("Nombre", max_length=255)
    nit = models.CharField(
        "Nit",
        max_length=15,
        help_text="El nit puede llevar el digito de verificación")
    state = models.ForeignKey(
        State,
        verbose_name="Departamento",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    city = models.ForeignKey(
        City,
        verbose_name="Ciudad",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    address = models.TextField("Dirección")
    phone = models.CharField(
        "Teléfono Fijo",
        max_length=7,
        help_text="Opcional. Sin indicativo de área",
        blank=True,
        null=True
    )
    cellphone = models.CharField(
        "Celular",
        max_length=10,
    )
    logo = models.ImageField(
        "logo de la empresa",
        upload_to=get_upload_to,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Centro de Enseñanaza Automovilísitico"
        verbose_name_plural = "Centros de Enseñanaza Automovilísiticos"


class Crc(models.Model):
    """Modelo para guardar los datos de los crc
    Centro de Reconocimiento de Conductores
    """

    MEDIA_PATH = 'crc'

    name = models.CharField("Nombre", max_length=255)
    nit = models.CharField(
        "Nit",
        max_length=15,
        help_text="El nit puede llevar el digito de verificación")
    price = models.CharField("Precio del servicio", max_length=7)
    price_double = models.CharField("Precio del servicio doble", max_length=7)
    state = models.ForeignKey(
        State,
        verbose_name="Departamento",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    city = models.ForeignKey(
        City,
        verbose_name="Ciudad",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    address = models.TextField("Dirección")
    phone = models.CharField(
        "Teléfono Fijo",
        max_length=7,
        help_text="Opcional. Sin indicativo de área",
        blank=True,
        null=True
    )
    cellphone = models.CharField(
        "Celular",
        max_length=10,
    )
    logo = models.ImageField(
        "logo de la empresa",
        upload_to=get_upload_to,
        blank=True,
        null=True
    )
    

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Centro de Reconocimiento de Conductores"
        verbose_name_plural = "Centros de Reconocimiento de Conductores"
    

class TransitDepartment(models.Model):
    """Modelo para guardar los datos de los departamentos
    de tránsito de las ciudades
    """
    MEDIA_PATH = 'transit'

    name = models.CharField("Nombre", max_length=255)
    nit = models.CharField(
        "Nit",
        max_length=15,
        help_text="El nit puede llevar el digito de verificación")
    state = models.ForeignKey(
        State,
        verbose_name="Departamento",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    city = models.ForeignKey(
        City,
        verbose_name="Ciudad",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    address = models.TextField("Dirección")
    phone = models.CharField(
        "Teléfono Fijo",
        max_length=7,
        help_text="Opcional. Sin indicativo de área",
        blank=True,
        null=True
    )
    cellphone = models.CharField(
        "Celular",
        max_length=10,
    )
    logo = models.ImageField(
        "logo de la empresa",
        upload_to=get_upload_to,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Departamento de Tránsito"
        verbose_name_plural = "Departamentos de Tránsito"


class Schedule(models.Model):
    """Guarda los horarios de disponibilidad de un establecimiento.
    El campo 'day' corresponde la número del día de la semana según el
    estándar ISO 8601, donde Lunes (monday) es 1, y Domingo (sunday) es 7
    """

    DAY_CHOICES = (
		(1, 'Lunes'),
		(2, 'Martes'),
		(3, 'Miercoles'),
		(4, 'Jueves'),
		(5, 'Viernes'),
		(6, 'Sábado'),
		(7, 'Domingo'),
	)

    JOURNEY = (
        ('J1', 'Jornada 1'),
        ('J2', 'Jornada 2')
    )

    day = models.CharField('Dia', choices=DAY_CHOICES, max_length=1)
    start_time = models.TimeField('Hora de inicio')
    end_time = models.TimeField('Hora de cierre')
    journey = models.CharField(
        'Jornada',
        max_length=2,
        choices=JOURNEY,
        default='J1'
    )
    cea = models.ForeignKey(
        Cea,
        on_delete=models.CASCADE,
        verbose_name="Centro de Enseñanaza Automovilísitico",
        related_name="related_%(class)ss",
        blank=True, null=True
    )
    crc = models.ForeignKey(
        Crc,
        on_delete=models.CASCADE,
        verbose_name="Centro de Reconocimiento de Conductores",
        related_name="related_%(class)ss",
        blank=True, null=True
    )
    transit = models.ForeignKey(
        TransitDepartment,
        verbose_name="Departamento de Tránsito",
        on_delete=models.CASCADE,
        related_name="related_%(class)ss",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = 'Horario'

    def __unicode__(self):
        if self.cea:
            return "Horario de %s" %(self.cea.name)
        elif self.crc:
            return "Horario de %s" %(self.crc.name)
        return "Horario de %s " %(self.transit.name)

    def clean(self):
        if self.cea and self.crc and self.transit:
            raise ValidationError('El horario no puede pertenecer a varias compañías a la vez. Selecciona solamente una')
        if not self.cea and not self.crc and not self.transit:
            raise ValidationError('Selecciona una compañía para estos horarios')

    def get_day(self):
        if not self.day:
            day = 1
        else:
            day = self.day
        day_dict = dict((x, y) for x, y in self.DAY_CHOICES)
        return day_dict.get(int(day))


class CeaLicence(models.Model):
    """Guarda las licencias que tiene disponibles 
    para la enseñanza cada cea
    """

    cea = models.ForeignKey(
        Cea,
        verbose_name="CEA",
        on_delete=models.CASCADE,
    )
    licence = models.ForeignKey(
        Licence,
        on_delete=models.CASCADE,
        verbose_name="Licencias",
        help_text="Selecciona las licencias disponibles en el CEA"
    )
    price = models.CharField(
        "Precio",
        max_length=255,
        help_text="Precio de la licencia nueva")
    price_recat = models.CharField(
        "Precio recategorización",
        max_length=255,
        help_text="Precio de la licencia para recategorización"
    )


    def __str__(self):
        return "Licencia %s de %s" % (self.licence, self.cea)

    
    class Meta:
        verbose_name = "Licencia de Cea"
        verbose_name_plural = "Licencias de los Cea"


class CeaVehicle(models.Model):
    """Guarda los vehículos disponibles de cada cea
    """

    cea = models.ForeignKey(
        Cea,
        verbose_name="CEA",
        on_delete=models.CASCADE,
    )
    vehicle = models.ForeignKey(
        Vehicle,
        verbose_name = "Vehículo",
        on_delete=models.CASCADE
    )
    badge = models.CharField(
        "Placa",
        max_length=7,
        help_text="ABC 123",
        unique=True
    )
    model = models.CharField(
        "Modelo",
        max_length=4,
        help_text="2008"
    )

    def __str__(self):
        return "%s %s del cea %s" % (self.vehicle.brand, self.vehicle.line, self.cea)

    
    class Meta:
        verbose_name = "Vehículo del CEA"
        verbose_name = "Vehículos del CEA"

