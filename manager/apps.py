# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig


class ManagerConfig(AppConfig):
    name = 'manager'
    verbose_name = 'Administrador'
    icon = '<i class="material-icons">build</i>'

    def ready(self):
        import manager.signals