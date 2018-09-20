
from rest_framework import serializers

from vehicles.serializers import VehicleSerializer
from .models import Crc, Cea, TransitDepartment, Schedule, CeaLicence, CeaVehicle


class CeaVehicleSerializer(serializers.ModelSerializer):
    """
    """

    vehicle = VehicleSerializer(many=False, read_only=True)

    class Meta:
        model = VehicleSerializer
        fields = ('id', 'vehicle', 'badge', 'model')


class CeaLicenceSerializer(serializers.ModelSerializer):
    """
    """

    licences = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='category'
    )

    class Meta:
        model = CeaLicence
        fields = ('licences', 'price', 'price_recat', 'theoretical_classes', 'practical_classes', 'mechanical_classes')


class CeaSerializer(serializers.ModelSerializer):
    """
    """

    licences = CeaLicenceSerializer(many=True, read_only=True)
    vehicles = CeaVehicleSerializer(many=True, read_only=True)


    class Meta:
        model = Cea
        fields = ('id', 'name', 'nit', 'state', 'city', 'address', 'phone', 'cellphone', 'logo')
