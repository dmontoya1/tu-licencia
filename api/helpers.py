import binascii
import os

from rest_framework.authentication import SessionAuthentication, BasicAuthentication 

from django.contrib.auth.middleware import get_user

def generate_key():
    return binascii.hexlify(os.urandom(20)).decode()


class CsrfExemptSessionAuthentication(SessionAuthentication):

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening