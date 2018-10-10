from rest_framework import serializers
from .models import Police, State, City, Sector


class PoliceSerializer(serializers.ModelSerializer):
    """
    Serializador para las politicas de la plataforma
    """

    class Meta:
        model = Police
        fields = ('id', 'name', 'police_type', 'text')


class StateSerializer(serializers.ModelSerializer):
    """
    Serializador para los departamentos
    """

    class Meta:
        model = State
        fields = ('id', 'name')


class CitySerializer(serializers.ModelSerializer):
    """
    Serializador para los municipios
    """

    state = StateSerializer(many=False, read_only=True)

    class Meta:
        model = City
        fields = ('id', 'name', 'state')


class SectorSerializer(serializers.ModelSerializer):
    """
    Serializador para los sectores
    """

    city = CitySerializer(many=False, read_only=True)

    class Meta:
        model = Sector
        fields = ('id', 'name', 'city')

