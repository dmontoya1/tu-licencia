from datetime import datetime

from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

from companies.models import Cea, Crc, TransitDepartment
from licences.models import Licence, AgeRange, AnsvRanges


class Request(models.Model):
    """Clase para guardar las solicitudes de los usuarios
    de sus licencias
    """

    CREDITO = "CR"
    CONTADO = "CO"

    PENDING = "PEN"
    PAID = "PAI"
    EN_CRC = "ICRC"
    EN_CEA = 'ICEA'
    FINISH = 'FNS'

    IN_LIQUID = 'ILIQU'
    PAID_SUCC = 'PSUCC'
    PAID_RETURN = 'PRETU'
    DOCS_SEND = 'DSEND'
    DOCS_DELIVERY = 'DDELI'
    DOCS_RETURN = 'DRETU'

    ACEPTADO = "AC"
    RECHAZADO = "RE"
    PENDIENTE_APROBACION = "PA"
    NO_APLICA = "NA"

    HAS_NOT_STARTER = "NS"
    STARTED = 'ST'
    FINISHED = 'FN'


    PAYMENTS = (
        (CREDITO, 'Sistecrédito'),
        (CONTADO, 'Contado')
    )

    REQUEST_STATUS = (
        (PENDING, 'Pendiente'),
        (PAID, 'Pagado'),
        (EN_CRC, 'En exámen CRC'),
        (EN_CEA, 'En curso CEA'),
        (FINISH, 'Finalizado')
    )

    DOCS_STATUS = (
        (PENDING, 'Pendiente'),
        (IN_LIQUID, 'En liquidación'),
        (PAID_SUCC, 'Pagos realizados'),
        (PAID_RETURN, 'Pagos retornados'),
        (DOCS_SEND, 'Documentación enviada'),
        (DOCS_DELIVERY, 'Documentación entregada'),
        (DOCS_RETURN, 'Documentación retornada'),
    )

    COMPANY_STATUS = (
        (HAS_NOT_STARTER, 'Sin iniciar'),
        (STARTED, 'Iniciado'),
        (FINISHED, 'Finalizado'),
    )

    CREDIT = (
        (ACEPTADO, 'Aceptado'),
        (RECHAZADO, 'Rechazado'),
        (PENDIENTE_APROBACION, 'Pendiente de aprobación'),
        (NO_APLICA, 'No aplica')
    )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Cliente",
        on_delete=models.CASCADE,
        related_name='related_requests',
        blank=True,
        null=True
    )
    total_price = models.IntegerField(
        "Precio total",
        default=0,
        
    )
    cea = models.ForeignKey(
        Cea,
        verbose_name="CEA",
        on_delete=models.SET_NULL,
        related_name='related_cea_requests',
        blank=True,
        null=True,
    )
    cea_status = models.CharField(
        "Estado trámite en el cea",
        max_length=2,
        choices=COMPANY_STATUS,
        default=HAS_NOT_STARTER
    )
    crc = models.ForeignKey(
        Crc,
        verbose_name="CRC",
        on_delete=models.SET_NULL,
        related_name='related_crc_requests',
        blank=True,
        null=True
    )
    crc_status = models.CharField(
        "Estado trámite en el crc",
        max_length=2,
        choices=COMPANY_STATUS,
        default=HAS_NOT_STARTER
    )
    transit = models.ForeignKey(
        TransitDepartment,
        verbose_name = "Departamento de Tránsito",
        on_delete=models.SET_NULL,
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
    request_status = models.CharField(
        "Estado de la reserva",
        choices=REQUEST_STATUS,
        max_length=4,
        default=PENDING
    )
    docs_status = models.CharField(
        "Estado de la documentación",
        choices=DOCS_STATUS,
        max_length=5,
        default=PENDING
    )
    credit_status = models.CharField(
        "Estado del crédito (si aplica)",
        choices=CREDIT,
        max_length=2,
        default=NO_APLICA
    )
    credit_request_code = models.CharField(
        "Código solicitud del crédito (si aplica)",
        help_text="Código del crédito (Systecrédito)",
        max_length=255,
        blank=True, null=True
    )
    booking = models.CharField(
        "Número de reserva", 
        max_length=255,
        blank=True, null=True
    )
    request_date = models.DateTimeField(
        "Fecha de la solicitud",
        auto_now_add=True,
    )
    has_runt = models.BooleanField(
        "Tiene RUNT?",
        default=False
    )

    def __init__(self, *args, **kwargs):
        super(Request, self).__init__(*args, **kwargs)
        try:
            self.__last_request_status = self.request_status
            self.__last_docs_status = self.docs_status
            self.__last_crc = self.crc
            self.__last_cea = self.cea
        except:
            pass

    def __str__(self):
        if self.user:
            return "Solicitud del usuario %s con documento %s" % (self.user, self.user.document_id)
        return " Solicitud %s " % (self.pk)

    
    class Meta:
        verbose_name = "Solicitud"
        verbose_name_plural = "Solicitudes"

    def add_new_status(self, status):
        log_request = LogRequestStatus(
            request_obj=self,
            status=status,
        )
        log_request.save()


    def save(self, *args, **kwargs):
        "Funcion para generar el booking de los clientes, y crear los logs en los cambios de estados"
        try:
            if self.request_status != self.__last_request_status:
                self.add_new_status(self.get_request_status_display())
            if self.crc_status == self.STARTED:
                self.request_status = self.EN_CRC
                self.add_new_status(self.get_request_status_display())
            if self.cea_status == self.STARTED and (self.crc_status == self.STARTED or self.crc_status == self.FINISH):
                self.request_status = self.EN_CEA
                self.add_new_status(self.get_request_status_display())
        except Exception as e:
            print ("Exception")
            print (e)

        super(Request, self).save(*args, **kwargs)
        try:
            d = self.request_date
            self.booking = 'RE{}{}{}{}'.format(d.month, d.day, self.user.pk, self.pk)
        except:
            pass
        super(Request, self).save(*args, **kwargs)


    def get_crc_price(self):
        if self.licences.all().count() == 1:
            return self.crc.price
        return self.crc.price_double

    get_crc_price.short_description = "Precio del CRC"


class RequestTramit(models.Model):
    """Guarda los trámites que se van a hacer en cada solicitud
    """

    FIRST_LICENCE = 'FL'
    SECOND_LICENCE = 'SL'
    RENEW = 'RN'
    RECAT = 'RC'
    DUPLICATED = 'DU'

    TRAMIT_TYPE = (
        (FIRST_LICENCE, 'Primera Licencia'),
        (SECOND_LICENCE, 'Segunda Licencia'),
        (RENEW, 'Renovación'),
        (RECAT, 'Recategorización'),
        (DUPLICATED, 'Duplicado')
    )

    request = models.ForeignKey(
        Request,
        verbose_name="Trámites",
        on_delete=models.CASCADE
    )
    tramit_type = models.CharField(
        "Tipo de Trámite",
        max_length=2,
        choices=TRAMIT_TYPE
    )
    licence = models.ForeignKey(
        Licence,
        verbose_name="Licencia",
        on_delete=models.SET_NULL,
        blank=True, null=True
    )

    def __str__(self):
        return "Tipo de trámite (%s => %s)" % (self.get_tramit_type_display(), self.licence.category)

    
    class Meta:
        verbose_name = 'Tramite'



class LogRequestStatus(models.Model):
    """Se guarda el log para los cambios de estado de la
    solicitud
    """

    request_obj = models.ForeignKey(
        Request,
        verbose_name="Solicitud",
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(
        "Fecha del cambio",
        auto_now_add=True,
    )
    status = models.CharField(
        "Estado",
        max_length=255,
    )

    def __str__(self):
        return "Cambio en %s al estado %s" % (self.request_obj, self.status)

    
    class Meta:
        verbose_name = "Log Estado de la solicitud"
        verbose_name_plural = "Logs de estados de la solicitud"


class LogDocsStatus(models.Model):
    """Se guarda el log para los cambios de estado de la 
    documentación
    """

    request_obj = models.ForeignKey(
        Request,
        verbose_name="Solicitud",
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(
        "Fecha del cambio",
        auto_now_add=True,
    )
    status = models.CharField(
        "Estado",
        max_length=255,
    )
    process_manager = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name="Responsable del proceso",
        on_delete=models.SET_NULL,
        blank=True, null=True,
    )
    transaction_manager = models.CharField(
        "Responsable de la operación",
        max_length=255,
        blank=True, null=True,
    )

    def __str__(self):
        return "Cambio en %s al estado %s" % (self.request_obj, self.status)

    
    class Meta:
        verbose_name = "Log Estado de la documentación"
        verbose_name_plural = "Logs de estados de la documentación"
