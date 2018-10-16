
from rest_framework import serializers

from manager.serializers import StateSerializer, CitySerializer
from licences.models import AnsvRanges, AgeRange, Licence
from licences.serializers import LicenceSerializer
from vehicles.serializers import VehicleSerializer
from .models import Crc, Cea, TransitDepartment, Schedule, CeaLicence, CeaVehicle, CeaRating, CrcRating, TransitRating


class CrcSerializer(serializers.ModelSerializer):
    """
    """
    final_price = serializers.SerializerMethodField()
    city = CitySerializer(many=False, read_only=True)

    def get_final_price(self, obj):
        request = self.context.get("request")
        age = request.GET.get('age')
        gender = request.GET.get('gender')
        licences = request.GET.get('licences')
        licences = licences.split(',')
        collection = obj.collection
        age_ranges = AgeRange.objects.all()

        for a in age_ranges:
            if int(age) in range(a.start_age, a.end_age+1):
                a_range = a
                break
        
        if len(licences) == 2:
            licence = Licence.objects.get(category=licences[0])
            ansv = AnsvRanges.objects.get(
                licence=licence,
                gender=gender,
                age_range=a_range,
            )
            exam_val = obj.price
        else:
            licence_1 = Licence.objects.get(category=licences[0])
            licence_2 = Licence.objects.get(category=licences[1])
            ansv1 = AnsvRanges.objects.get(
                licence=licence_1,
                gender=gender,
                age_range=a_range,
            )
            ansv2 = AnsvRanges.objects.get(
                licence=licence_2,
                gender=gender,
                age_range=a_range,
            )
            exam_val = obj.price_double

            if ansv1.price > ansv2.price:
                ansv = ansv1
            else:
                ansv = ansv2
        return exam_val + collection.pin_sicov + collection.recaudo + ansv.price

    class Meta:
        model = Crc
        fields = ('id', 'name', 'nit', 'state', 'city', 'address', 'phone', 'cellphone', 'logo', 'final_price', 'rating')


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
    city = CitySerializer(many=False, read_only=True)

    class Meta:
        model = Cea
        fields = ('id', 'name', 'nit', 'state', 'city', 'address', 'phone', 'cellphone', 'logo', 'licences', 'vehicles', 'rating')


class TransitSerializer(serializers.ModelSerializer):
    """
    """

    city = CitySerializer(many=False, read_only=True)

    class Meta:
        model = TransitDepartment
        fields = ('id', 'name', 'nit', 'state', 'city', 'address', 'phone', 'cellphone', 'logo', 'runt_price', 'rating')

