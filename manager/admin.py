# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib import messages
from django.db.models import Q
from .models import State, City, Police


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

    def save_model(self, request, obj, form, change):
        messages.set_level(request, messages.WARNING)
        messages.warning(request, 'Departamento grabado exitosamente')
        super(StateAdmin, self).save_model(request, obj, form, change)


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

    def save_model(self, request, obj, form, change):
        messages.set_level(request, messages.WARNING)
        messages.warning(request, 'Ciudad grabado exitosamente')
        super(CityAdmin, self).save_model(request, obj, form, change)


@admin.register(Police)
class PoliceAdmin(admin.ModelAdmin):
    """
    Clase para administrar las políticas de la plataforma
    """

    model = Police
    icon = '<i class="material-icons">account_balance</i>'
    search_fields = (
        'name', 'police_type'
    )
    list_display = (
        'name', 'police_type'
    )
    fieldsets = (
        (None, {
            'fields': (
                'police_type', 'name', 'text'
            ),
        }),
    )

    def save_model(self, request, obj, form, change):
        messages.set_level(request, messages.WARNING)
        messages.warning(request, 'Política grabada exitosamente')
        super(PoliceAdmin, self).save_model(request, obj, form, change)
