# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import messages
from django.db.models import Q
from .models import State, City, Police, CRCAdminPrices


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    """
    Clase para la administración de los Departamentos
    """

    model = State
    icon = '<i class="material-icons">beenhere</i>'
    search_fields = (
        'name', 'related_cities__name'
    )
    list_display = (
        'name', 'code',
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False



@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    """
    Clase para la admintración de los municipios
    """

    model = City
    icon = '<i class="material-icons">place</i>'
    search_fields = (
        'state__name', 'name',
    )
    list_display = (
        'name', 'state', 'code'
    )

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False



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


@admin.register(CRCAdminPrices)
class CRCAdminPricesAdmin(admin.ModelAdmin):
    """
    Administra los datos de pin sicov y recaudo de las CRC
    """

    model = CRCAdminPrices
    list_display = ('id', 'pin_sicov', 'recaudo')
