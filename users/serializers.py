from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    """
    Serializador para las politicas de la plataforma
    """

    class Meta:
        model = User
        fields = (
            'id', 'first_name', 'last_name', 'email', 'password',
            'gender', 'document_type', 'document_id', 'cellphone',
            'city', 'state', 'birth_date'
        )
