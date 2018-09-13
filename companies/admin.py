# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Cea, Crc, TransitDepartment, Schedule, CeaLicence, CeaVehicle


class ScheduleAdmin(admin.StackedInline):
    
    model = Schedule
    extra = 0
    fieldsets = (
        (None, {
            'fields': (
                'id', 'day', 'start_time', 'end_time', 'journey'
            ),
        }),
    )


class CeaLicenceAdmin(admin.StackedInline):
    """
    """

    model = CeaLicence
    extra = 1


class CeaVehicleAdmin(admin.StackedInline):
    """
    """
    model = CeaVehicle
    extra = 1


@admin.register(Cea)
class CeaAdmin(admin.ModelAdmin):
    """
    """

    model = Cea
    list_display = ('nit', 'name', 'cellphone')
    inlines = [ScheduleAdmin, CeaLicenceAdmin, CeaVehicleAdmin]


@admin.register(Crc)
class CrcAdmin(admin.ModelAdmin):
    """
    """

    model = Crc
    list_display = ('nit', 'name', 'cellphone')
    inlines = [ScheduleAdmin,]


@admin.register(TransitDepartment)
class TransitDepartmentAdmin(admin.ModelAdmin):
    """
    """

    model = TransitDepartment
    list_display = ('nit', 'name', 'cellphone')
    inlines = [ScheduleAdmin,]
