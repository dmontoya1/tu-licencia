
from rest_framework import serializers

from licences.serializers import LicenceSerializer
from vehicles.serializers import VehicleSerializer
from .models import Crc, Cea, TransitDepartment, Schedule, CeaLicence, CeaVehicle


class CeaVehicleSerializer(serializers.ModelSerializer):
    """
    """

    vehicle = VehicleSerializer(many=False, read_only=True)

    class Meta:
        model = CeaVehicle
        fields = ('id', 'vehicle', 'badge', 'model')


class CeaLicenceSerializer(serializers.ModelSerializer):
    """
    """

    licence = LicenceSerializer(many=False, read_only=True)

    class Meta:
        model = CeaLicence
        fields = ('licence', 'price', 'price_recat', 'theoretical_classes', 'practical_classes', 'mechanical_classes')


class CeaSerializer(serializers.ModelSerializer):
    """
    """

    licences = CeaLicenceSerializer(many=True, read_only=True)
    vehicles = CeaVehicleSerializer(many=True, read_only=True)


    class Meta:
        model = Cea
        fields = ('id', 'name', 'nit', 'state', 'city', 'address', 'phone', 'cellphone', 'logo', 'licences', 'vehicles')


class CrcSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = Crc
        fields = ('id', 'name', 'nit', 'state', 'city', 'address', 'phone', 'cellphone', 'logo', 'price', 'price_double')


class TransitSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = TransitDepartment
        fields = ('id', 'name', 'nit', 'state', 'city', 'address', 'phone', 'cellphone', 'logo',)

