# -*- coding: utf-8 -*-
from __future__ import unicode_literals

def get_upload_to(instance, filename):
    """
    Obtener la url donde se van a guardar los media
    """

    return '{0}/{1}/{2}'.format(instance.MEDIA_PATH, instance.nit, filename)