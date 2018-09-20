from django.db import models

from .utils import get_upload_to

from licences.models import Licence


class Brand(models.Model):
    """Se almacenan las marcas de vehículos 
    (Kia, Chevrolet, Renault, etc)
    """

    name = models.CharField(
        "Nombre de la marca",
        max_length=255,
        help_text="Kia, Chevrolet, Renault..."
    )

    def __str__(self):
        return self.name

    
    class Meta:
        verbose_name = "Marca de vehículo"
        verbose_name_plural = "Marcas de vehículo"


class Vehicle(models.Model):
    """
    """

    brand = models.ForeignKey(
        Brand,
        verbose_name = "Marca del vehículo",
        on_delete=models.CASCADE,
    )
    line = models.CharField(
        "Linea del vehículo",
        max_length=255,
        help_text="Picanto, Spark GT, Clio, Twingo...."
    )
    licences = models.ManyToManyField(
        Licence,
        verbose_name="Licencias",
        help_text="Escoga una o varias licencias válidas para éste vehículo"
    )

    def __str__(self):
        return "%s %s" % (self.brand, self.line)

    
    class Meta:
        verbose_name = "Vehículo"


class VehicleImages(models.Model):
    """Imágenes de los vehículos
    """
    vehicle = models.ForeignKey(
        Vehicle,
        verbose_name="Vehículo",
        on_delete=models.CASCADE,
        related_name="images"
    )
    image = models.ImageField(
        "Imágen",
        upload_to=get_upload_to,
    )

    def __str__(self):
        return "Imagen de %s %s" % (self.vehicle.brand, self.vehicle.line)

    
    class Meta:
        verbose_name = "Imagen de vehículo"
        verbose_name_plural = "Imágenes de vechículos"
    

