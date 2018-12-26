# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Avg

from licences.models import Licence
from manager.models import State, City, CompaniesAdminPrices, Sector, TransitDepartmentPrices
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
    rating = models.FloatField(
        "Calificación Promedio",
        default=0
    )
    collection = models.ForeignKey(
        CompaniesAdminPrices,
        verbose_name="Pin sicov y recaudo banco",
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    schedule = models.TextField(
        "Horarios de atención administrativo",
        help_text="Ejm: De lunes a viernes de 8:00 am a 6:00 pm"
    )
    courses_schedule = models.TextField(
        "Horarios de atención para cursos",
        help_text="Ejm: De lunes a viernes de 8:00 am a 6:00 pm"
    )
    epayco_code = models.CharField(
        'Codigo ePayco',
        max_length=10,
    )

    def __str__(self):
        return self.name

    def get_pin_sicov(self):
        return '$ %s' % (self.collection.pin_sicov)
    
    def get_recaudo(self):
        return '$ %s' % (self.collection.recaudo)

    
    get_pin_sicov.short_description = "Pin Sicov"
    get_recaudo.short_description = "Recaudo banco"


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
        default=1,
        on_delete=models.SET_DEFAULT,
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
        CompaniesAdminPrices,
        verbose_name="Pin sicov y recaudo banco",
        on_delete=models.SET_NULL,
        blank=True, null=True
    )
    rating = models.FloatField(
        "Calificación Promedio",
        default=0
    )
    schedule = models.TextField(
        "Horarios de atención",
        help_text="Ejm: De lunes a viernes de 8:00 am a 6:00 pm"
    )
    epayco_code = models.CharField(
        'Codigo ePayco',
        max_length=10,
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
    rating = models.FloatField(
        "Calificación Promedio",
        default=0
    )
    schedule = models.TextField(
        "Horarios de atención",
        help_text="Ejm: De lunes a viernes de 8:00 am a 6:00 pm"
    )
    prices = models.ForeignKey(
        TransitDepartmentPrices, 
        verbose_name='Precios organismo de transito',
        blank=True, null=True,
        on_delete=models.SET_NULL
    )

    def get_runt(self):
        return '$ %s' % (self.prices.runt)
    
    def get_printing(self):
        return '$ %s' % (self.prices.printing)

    def get_other_values(self):
        return '$ %s' % (self.prices.other)


    get_runt.short_description = "RUNT"
    get_printing.short_description = "Impresion"
    get_other_values.short_description = "Otros valores"

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
    price = models.IntegerField(
        "Precio",
        help_text="Precio de la licencia nueva")
    price_recat = models.IntegerField(
        "Precio recategorización",
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
    is_active = models.BooleanField(
        "Esta activo?",
        default=True
    )

    def __str__(self):
        return "%s %s del cea %s" % (self.vehicle.brand, self.vehicle.line, self.cea)

    
    class Meta:
        verbose_name = "Vehículo del CEA"
        verbose_name = "Vehículos del CEA"


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
        related_name="cea_ratings"
        )
    detail = models.TextField(null=True, default="N/A")
    stars = models.IntegerField()

    def __str__(self):
        return "%s - %s" % (self.user, self.stars)

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
        related_name="crc_ratings"
        )
    detail = models.TextField(null=True, default="N/A")
    stars = models.IntegerField()

    def __str__(self):
        return "%s - %s" % (self.user, self.stars)

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
        related_name="transit_ratings"
        )
    detail = models.TextField(null=True, default="N/A")
    stars = models.IntegerField()

    def __str__(self):
        return "%s - %s" % (self.user, self.stars)

    class Meta:
        verbose_name = "Calificacion Organismo de transporte"
        verbose_name_plural = "Calificaciones Organismo de transporte"

