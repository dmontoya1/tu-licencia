from rest_framework import serializers

from .models import Licence


class LicenceSerializer(serializers.ModelSerializer):
    """
    """

    class Meta:
        model = Licence
        fields = ('id', 'category', 'description')
