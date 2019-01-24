
from rest_framework import serializers

from manager.models import CompaniesAdminPrices
from manager.serializers import StateSerializer, CitySerializer, SectorSerializer
from licences.models import AnsvRanges, AgeRange, Licence
from licences.serializers import LicenceSerializer
from vehicles.serializers import VehicleSerializer
from .models import Crc, Cea, TransitDepartment, CeaLicence, CeaVehicle, CeaRating, CrcRating, TransitRating


class CrcSerializer(serializers.ModelSerializer):
    """
    """
    final_price = serializers.SerializerMethodField()
    city = CitySerializer(many=False, read_only=True)
    sector = SectorSerializer(many=False, read_only=True)
    count_rating = serializers.SerializerMethodField()

    def get_final_price(self, obj):
        request = self.context.get("request")
        age = request.GET.get('age')
        gender = request.GET.get('gender')
        licences = request.GET.get('licences')
        licences = licences.split(',')
        if obj.collection:
            collection = obj.collection
        else:
            collection = CompaniesAdminPrices.objects.first()

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

    def get_count_rating(self, obj):
        return CrcRating.objects.filter(crc=obj).count()

    class Meta:
        model = Crc
        fields = ('id', 'name', 'nit', 'state', 'city', 'sector', 'address', 'phone', 'cellphone', 'logo', 'final_price', 'rating', 'schedule', 'count_rating', 'lat', 'lon')


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
    sector = SectorSerializer(many=False, read_only=True)
    final_price = serializers.SerializerMethodField()
    count_rating = serializers.SerializerMethodField()

    def get_final_price(self, obj):
        request = self.context.get("request")
        age = request.GET.get('age')
        gender = request.GET.get('gender')
        licences = request.GET.get('licences')
        licences = licences.split(',')
        final_price = 0
        if obj.collection:
            collection = obj.collection
        else:
            collection = CompaniesAdminPrices.objects.filter(company=CompaniesAdminPrices.CEA).first()
        
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
            cealicence = CeaLicence.objects.filter(cea=obj, licence=licence).first()
            if cealicence:
                course_price = cealicence.price
            else:
                course_price = 0
            
            final_price = course_price + collection.pin_sicov + collection.recaudo + ansv.price
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
            cealicence1 = CeaLicence.objects.filter(cea=obj, licence=licence_1).first()
            cealicence2 = CeaLicence.objects.filter(cea=obj, licence=licence_2).first()
            if cealicence1:
                course_price1 = cealicence1.price
            else:
                course_price1 = 0
            if cealicence2:
                course_price2 = cealicence2.price
            else:
                course_price2 = 0

            price1 = course_price1 + collection.pin_sicov + collection.recaudo + ansv1.price
            price2 = course_price2 + collection.pin_sicov + collection.recaudo + ansv2.price

            final_price = price1 + price2
        
        return final_price

    def get_count_rating(self, obj):
        return CeaRating.objects.filter(cea=obj).count()

    class Meta:
        model = Cea
        fields = ('id', 'name', 'nit', 'state', 'city', 'sector', 'address', 'phone', 'cellphone', 'logo', 'licences', 'vehicles', 'rating', 'schedule', 'final_price', 'count_rating', 'courses_schedule', 'lat', 'lon')


class TransitSerializer(serializers.ModelSerializer):
    """
    """

    city = CitySerializer(many=False, read_only=True)
    count_rating = serializers.SerializerMethodField()
    sector = SectorSerializer(many=False, read_only=True)
    final_price = serializers.SerializerMethodField()

    def get_final_price(self, obj):
        return obj.prices.runt + obj.prices.printing + obj.prices.other


    def get_count_rating(self, obj):
        return TransitRating.objects.filter(transit=obj).count()

    class Meta:
        model = TransitDepartment
        fields = ('id', 'name', 'nit', 'state', 'city', 'sector', 'address', 'phone', 'cellphone', 'logo', 'final_price', 'rating', 'schedule', 'count_rating', 'lat', 'lon')


class CeaDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cea
        fields = ('id', 'name', 'nit')


class CrcDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Crc
        fields = ('id', 'name', 'nit')


class TransitDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = TransitDepartment
        fields = ('id', 'name', 'nit')


class CeaRatingSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = CeaRating
        fields = ('user', 'cea', 'detail', 'stars', )


class CrcRatingSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = CrcRating
        fields = ('user', 'crc', 'detail', 'stars', )


class TransitRatingSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = TransitRating
        fields = ('user', 'transit', 'detail', 'stars', )
