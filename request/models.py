from django.db import models

from django.conf import settings

from companies.models import Cea, Crc, TransitDepartment
from licences.models import Licence


class Request(models.Model):
    """Clase para guardar las solicitudes de los usuarios
    de sus licencias
    """

    CREDITO = "CR"
    CONTADO = "CO"
    ACEPTADA = "AC"
    ATENDIDA = "AT"
    PENDIENTE = "PE"
    ACEPTADO = "AC"
    RECHAZADO = "RE"
    PENDIENTE_APROBACION = "PA"
    NO_APLICA = "NA"

    PAYMENTS = (
        (CREDITO, 'Sistecrédito'),
        (CONTADO, 'Contado')
    )

    STATUS = (
        (ACEPTADA, 'Aceptado'),
        (ATENDIDA, 'Atendido'),
        (PENDIENTE, 'Pendiente')
    )

    CREDIT = (
        (ACEPTADO, 'Aceptado'),
        (RECHAZADO, 'Rechazado'),
        (PENDIENTE_APROBACION, 'Pendiente de aprobación'),
        (NO_APLICA, 'No aplica')
    )

    cea = models.ForeignKey(
        Cea,
        verbose_name="CEA",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    crc = models.ForeignKey(
        Crc,
        verbose_name="CRC",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    transit = models.ForeignKey(
        TransitDepartment,
        verbose_name = "Departamento de Tránsito",
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Cliente",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    payment_type = models.CharField(
        "Tipo de pago",
        choices=PAYMENTS,
        max_length=2,
    )
    licences = models.ManyToManyField(
        Licence,
        verbose_name="Licencias solicitadas",
        related_name="related_licences",
    )
    status = models.CharField(
        "Estado",
        choices=STATUS,
        max_length=2
    )
    credit_status = models.CharField(
        "Estado del crédito (si aplica)",
        choices=CREDIT,
        max_length=2
    )


    def __str__(self):
        if self.user:
            return "Solicitud del usuario %s con documento %s" % (self.user, self.user.document_id)
        return " Solicitud %s " % (self.pk)

    
    class Meta:
        verbose_name = "Solicitud"
        verbose_name_plural = "Solicitudes"


    def get_crc_price(self):
        if self.licences.all().count() == 1:
            return self.crc.price
        return self.crc.price_double

    get_crc_price.short_description = "Precio del CRC"

