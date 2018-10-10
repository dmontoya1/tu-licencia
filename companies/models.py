# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models

from licences.models import Licence
from manager.models import State, City, CRCAdminPrices, Sector
from utils.models import SoftDeletionModelMixin
from vehicles.models import Vehicle
from .utils import get_upload_to


class Cea(SoftDeletionModelMixin):
    """Modelo para guardar los datos de los cea
    Centro de Enseñanaza Automovilísitico
    """

    MEDIA_PATH = 'cea'

    name = models.CharField("Nombre", max_length=255)
    nit = models.CharField(
        "Nit",
        max_length=15,
        help_text="El nit puede llevar el digito de verificación")
    manager = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Administrador",
        blank=True,
        null=True
    )
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
    sector = models.ForeignKey(
        Sector,
        verbose_name="Sector",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    address = models.CharField("Dirección", max_length=255)
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
    email = models.CharField(
        "Correo Electrónico",
        max_length=255,
        blank=True, null=True
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


class Crc(SoftDeletionModelMixin):
    """Modelo para guardar los datos de los crc
    Centro de Reconocimiento de Conductores
    """

    MEDIA_PATH = 'crc'

    name = models.CharField("Nombre", max_length=255)
    nit = models.CharField(
        "Nit",
        max_length=15,
        help_text="El nit puede llevar el digito de verificación"
    )
    manager = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Administrador",
        blank=True,
        null=True
    )
    price = models.IntegerField(
        "Precio del servicio",
        help_text="Precio del servicio para una sola licencia"
    )
    price_double = models.IntegerField(
        "Precio del servicio doble",
        help_text="Precio del servicio para 2 licencias"
    )
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
    sector = models.ForeignKey(
        Sector,
        verbose_name="Sector",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    email = models.CharField(
        "Correo Electrónico",
        max_length=255,
        blank=True, null=True
    )
    address = models.CharField("Dirección", max_length=255)
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
    collection = models.ForeignKey(
        CRCAdminPrices,
        verbose_name="Pin sicov y recaudo banco",
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    

    def get_pin_sicov(self):
        return '$ %s' % (self.collection.pin_sicov)
    
    def get_recaudo(self):
        return '$ %s' % (self.collection.recaudo)

    def __str__(self):
        return self.name
    
    get_pin_sicov.short_description = "Pin Sicov"
    get_recaudo.short_description = "Recaudo banco"


    class Meta:
        verbose_name = "Centro de Reconocimiento de Conductores"
        verbose_name_plural = "Centros de Reconocimiento de Conductores"
    

class TransitDepartment(SoftDeletionModelMixin):
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
    sector = models.ForeignKey(
        Sector,
        verbose_name="Sector",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    email = models.CharField(
        "Correo Electrónico",
        max_length=255,
        blank=True, null=True
    )
    address = models.CharField("Dirección", max_length=255)
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
    runt_price = models.CharField(
        "Precio del RUNT",
        max_length=255
    )

    def __str__(self):
        return self.name


    class Meta:
        verbose_name = "Departamento de Tránsito"
        verbose_name_plural = "Departamentos de Tránsito"


class TuLicencia(SoftDeletionModelMixin):
    """Administrador de los puntos de TuLicencia
    """

    address = models.CharField("Dirección", max_length=255)
    phone = models.CharField(
        "Teléfono fijo",
        max_length=7,
        help_text="Opcional. Sin indicativo de área",
        blank=True,
        null=True
    )
    cellphone = models.CharField(
        "Celular",
        max_length=10,
    )
    express_user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        verbose_name="Usuario Express",
        blank=True,
        null=True
    )
    state = models.ForeignKey(
        State,
        verbose_name="Departamento",
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    email = models.CharField(
        "Correo Electrónico",
        max_length=255,
        blank=True, null=True
    )
    city = models.ForeignKey(
        City,
        verbose_name="Ciudad",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return "Punto Tu licencia en %s - %s (%s)" % (self.state, self.city, self.address)


    class Meta:
        verbose_name = "Punto TuLicencia"
        verbose_name_plural = "Puntos TuLicencia"


class Schedule(models.Model):
    """Guarda los horarios de disponibilidad de un establecimiento.
    El campo 'day' corresponde la número del día de la semana según el
    estándar ISO 8601, donde Lunes (monday) es 1, y Domingo (sunday) es 7
    """

    DAY_CHOICES = (
		("1", 'Lunes'),
		("2", 'Martes'),
		("3", 'Miercoles'),
		("4", 'Jueves'),
		("5", 'Viernes'),
		("6", 'Sábado'),
		("7", 'Domingo'),
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
        if (self.cea and self.crc ) or (self.cea and self.transit) or (self.crc and self.transit):
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
        related_name='licences'
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
    theoretical_classes = models.IntegerField("Número de clases teóricas")
    practical_classes = models.IntegerField("Número de clases prácticas")
    mechanical_classes = models.IntegerField("Número de clases de Taller")

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
        related_name='vehicles'
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


class TransitLicence(models.Model):
    """Guarda los precios de las licencias de los departamentos
    de tránsito
    """

    transit = models.ForeignKey(
        TransitDepartment,
        verbose_name="Oficina de Tránsito",
        on_delete=models.CASCADE,
        related_name='related_licences'
    )
    licence = models.ForeignKey(
        Licence,
        on_delete=models.CASCADE,
        verbose_name="Licencias",
        help_text="Selecciona la licencia"
    )
    price = models.CharField(
        "Precio",
        max_length=255,
        help_text="Precio de la licencia nueva")

    def __str__(self):
        return "Licencia %s de %s" % (self.licence, self.transit)


    class Meta:
        verbose_name = "Precio de licencia de tránsito"
        verbose_name_plural = "Precios de licencias de tránsito"


class CeaRating(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Usuario",
        on_delete=models.CASCADE,
        related_name='related_cea_user_ratings'
    )
    cea = models.ForeignKey(
        Cea,
        verbose_name="Cea",
        on_delete=models.CASCADE,
        related_name="related_cea_ratings"
        )
    detail = models.TextField(null=True, default="N/A")
    stars = models.IntegerField()

    def __str__(self):
        return "%s - %s" % self.user, self.stars

    class Meta:
        verbose_name = "Calificacion CEA"
        verbose_name_plural = "Calificaciones CEA"


class CrcRating(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Usuario",
        on_delete=models.CASCADE,
        related_name='related_crc_user_ratings'
    )
    crc = models.ForeignKey(
        Crc,
        verbose_name="Crc",
        on_delete=models.CASCADE,
        related_name="related_crc_ratings"
        )
    detail = models.TextField(null=True, default="N/A")
    stars = models.IntegerField()

    def __str__(self):
        return "%s - %s" % self.user, self.stars

    class Meta:
        verbose_name = "Calificacion CRC"
        verbose_name_plural = "Calificaciones CRC"
        
        
class TransitRating(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Usuario",
        on_delete=models.CASCADE,
        related_name='related_transit_user_ratings'
    )
    transit = models.ForeignKey(
        TransitDepartment,
        verbose_name="Organismo de transporte",
        on_delete=models.CASCADE,
        related_name="related_transit_ratings"
        )
    detail = models.TextField(null=True, default="N/A")
    stars = models.IntegerField()

    def __str__(self):
        return "%s - %s" % self.user, self.stars

    class Meta:
        verbose_name = "Calificacion Organismo de transporte"
        verbose_name_plural = "Calificaciones Organismo de transporte"

