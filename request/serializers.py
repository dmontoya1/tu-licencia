
from rest_framework import serializers

from users.serializers import UserSerializer

from .models import Request

class RequestSerializer(serializers.ModelSerializer):
    """
    Serializador para las politicas de la plataforma
    """



    user = UserSerializer(many=False,)

    class Meta:
        model = Request
        fields = (
            'id', 'user', 'cea', 'crc', 'transit', 'payment_type',
            'licences',)
