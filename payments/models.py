# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import time

from django.conf import settings
from django.db import models

    
# class Invoice(models.Model):
#     """Guarda las facturas generadas a cada usuario.
#     """

#     MONTHLY = 'MO'
#     YEARLY = 'YE'

#     RECURRENCY_TYPE_CHOICES = (
#         (MONTHLY, 'Por mes'),
#         (YEARLY, 'Por año')
#     )

#     APPROVED = 'AP'
#     PENDING  = 'PE'
#     CANCEL  = 'CA'
#     REJECTED  = 'RE'

#     STATUS = (
#         (APPROVED, 'Aprobada'),
#         (PENDING,  'Pendiente'),
#         (CANCEL,  'Cancelada'),
#         (REJECTED,  'Rechazada'),
#     )

#     DEFAULT_RELATED_NAME = "related_%(class)ss"


#     recurrency_type = models.CharField(
#         'Tipo de recurrencia',
#         max_length=2,
#         choices=RECURRENCY_TYPE_CHOICES,
#         blank=True, null=True
#     )
#     is_discharged = models.BooleanField('¿Está pago?', default=False)
#     release_date = models.DateTimeField('Fecha de generación', auto_now_add=True)
#     payment_date = models.DateTimeField(
#         'Fecha de pago',
#         null=True,
#         blank=True
#     )
#     payu_reference_code = models.CharField(
#         'Referencia Pago payU',
#         max_length=255,
#         blank=True,
#         null=True
#     )
#     payment_status = models.CharField(
#         'Estado del Pago',
#         max_length=50,
#         choices=STATUS,
#         default=PENDING
#     )

#     class Meta:
#         verbose_name = 'Factura'

#     def __unicode__(self):
#         return self.get_identifier()
    
#     def get_identifier(self):
#         return 'IN_{}{}'.format(
#             self.pk,
#             int(time.mktime(self.release_date.timetuple()))
#         )
    
#     def get_payment_date(self):
#         pass


