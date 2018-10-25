# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from utils.models import SoftDeletionModelMixin


class State(SoftDeletionModelMixin):
    """
    Clase para los departamentos
    """

    code = models.IntegerField("Codigo", null=True, blank=True, unique=True)
    name = models.CharField("Nombre", max_length=50)

    def __str__(self):
        return "%s" % (self.name)

    def soft_delete(self):
        """Ejecuta un borrado lógico desde la instancia
        """

        self.deleted_at = timezone.now()
        self.save()
        for city in self.related_cities.all():
            city.deleted_at = timezone.now()
            city.save()

    def revive(self):
        """Habilita un objeto que esté lógicamente borrado
        """

        self.deleted_at = None
        self.save()


    class Meta:
        verbose_name = "Departamento"


class City(SoftDeletionModelMixin):
    """
    Clase para los municipios
    """

    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='related_cities',
                              verbose_name="Departamento")
    code = models.CharField("Código", max_length=4, null=True, blank=True)
    name = models.CharField("Nombre", max_length=50)

    def __str__(self):
        return "%s" % (self.name)

    
    def soft_delete(self):
        """Ejecuta un borrado lógico desde la instancia
        """

        self.deleted_at = timezone.now()
        self.save()
        for sector in self.related_sectors.all():
            sector.deleted_at = timezone.now()
            sector.save()

    def revive(self):
        """Habilita un objeto que esté lógicamente borrado
        """

        self.deleted_at = None
        self.save()
        for sector in self.related_sectors.all():
            sector.deleted_at = None
            sector.save()


    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"


class Sector(SoftDeletionModelMixin):
    """
    Clase para los sectores
    """

    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='related_sectors',
                              verbose_name="Ciudad")
    name = models.CharField("Nombre Sector", max_length=255)

    def __str__(self):
        return "%s" % (self.name)


    class Meta:
        verbose_name = "Sector"
        verbose_name_plural = "Sectores"


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


class CompaniesAdminPrices(models.Model):
    """Modelo para guardar los valores de
    Pin Sicov y Recaudo de Banco para el cálculo del valor
    total a pagar del CRC
    """

    CEA = 'CEA'
    CRC = 'CRC'

    COMPANIES = (
        (CEA, 'Centro de enseñanza automovilístico'),
        (CRC, 'Centro de reconocimiento de conductores')
    )

    pin_sicov = models.IntegerField(
        "Precio PIN SICOV",
    )
    recaudo = models.IntegerField(
        "Precio Recaudo Banco",
    )
    supplier = models.CharField(
        "Proveedor",
        max_length=255,
        default=""
    )
    company = models.CharField(
        "Compañía",
        max_length=3,
        choices=COMPANIES,
        default=CRC
    )


    def __str__(self):
        return "Recaudo de %s para %s" % (self.supplier, self.company)
    

    class Meta:
        verbose_name = "Adminsitración Recaudo"
        verbose_name_plural = "Administración Recaudos"
