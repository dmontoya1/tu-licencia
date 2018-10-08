
from rest_framework import serializers


from .models import Brand, Vehicle, VehicleImages


class VehicleImagesSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = VehicleImages
        fields = ('id', 'image')


class BrandSerializer(serializers.ModelSerializer):
    """
    """
    class Meta:
        model = Brand
        fields = ('id', 'name')


class VehicleSerializer(serializers.ModelSerializer):
    """
    """

    brand = BrandSerializer(many=False)
    images = VehicleImagesSerializer(many=True, read_only=True)

    class Meta:
        model = Vehicle
        fields = ('id', 'brand', 'line', 'images')
