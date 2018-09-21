# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def get_upload_to(instance, filename):
    """
    Obtener la url donde se van a guardar los media
    """

    return '{0}/{1}/{2}'.format(instance.MEDIA_PATH, instance.nit, filename)

def params_to_filter(params):
    """Función para pasar el queryset a filter
    """
    filters = {}
    for k,v in params:
        if ',' in str(v):
            v = v.split(',')
        filters[k] = v
    return filters
