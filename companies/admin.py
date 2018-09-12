# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Cea, Crc, TransitDepartment, Schedule


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



@admin.register(Cea)
class CeaAdmin(admin.ModelAdmin):
    """
    """

    model = Cea
    list_display = ('nit', 'name', 'cellphone')
    inlines = [ScheduleAdmin,]


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
