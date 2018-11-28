# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import messages
from django.db.models import Q
from .models import State, City, Police, CompaniesAdminPrices, Sector, ContactForm, TransitDepartmentPrices

from utils.admin import SoftDeletionModelAdminMixin


@admin.register(State)
class StateAdmin(SoftDeletionModelAdminMixin):
    """
    Clase para la administración de los Departamentos
    """

    model = State
    search_fields = (
        'name', 'related_cities__name'
    )
    extra_list_display = (
        'name', 'code',
    )
    ordering = ('name',)

    def has_add_permission(self, request):
        return False


@admin.register(City)
class CityAdmin(SoftDeletionModelAdminMixin):
    """
    Clase para la admintración de los municipios
    """

    model = City
    search_fields = (
        'state__name', 'name',
    )
    extra_list_display = (
        'name', 'state', 'code'
    )
    ordering = ('state', 'name')

    def has_add_permission(self, request):
        return False


@admin.register(Sector)
class SectorAdmin(SoftDeletionModelAdminMixin):
    """
    Clase para la admintración de los sectores
    """

    model = Sector
    search_fields = (
        'city__name', 'name',
    )
    extra_list_display = (
        'name', 'city',
    )


@admin.register(Police)
class PoliceAdmin(admin.ModelAdmin):
    """
    Clase para administrar las políticas de la plataforma
    """

    model = Police
    icon = '<i class="material-icons">account_balance</i>'
    search_fields = (
        'police_type',
    )
    list_display = (
        'police_type',
    )
    fieldsets = (
        (None, {
            'fields': (
                'police_type', 'text'
            ),
        }),
    )


@admin.register(CompaniesAdminPrices)
class CompaniesAdminPricesAdmin(admin.ModelAdmin):
    """
    Administra los datos de pin sicov y recaudo de las CRC
    """

    model = CompaniesAdminPrices
    list_display = ('supplier', 'company', 'pin_sicov', 'recaudo')


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    """Administra los formularios de contacto de los clientes
    """

    model = ContactForm
    list_display = ('full_name', 'email', 'contact_type', 'date')

    readonly_fields = ('full_name', 'email', 'contact_type', 'message', 'date')


@admin.register(TransitDepartmentPrices)
class TransitDepartmentPricesAdmin(admin.ModelAdmin):
    """Adminsitra los precios para los organismos de transito
    """

    model = TransitDepartmentPrices
    list_display = ('name', 'runt', 'printing', 'other')
