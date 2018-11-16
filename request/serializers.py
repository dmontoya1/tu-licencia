
from rest_framework import serializers

from companies.serializers import CeaDetailSerializer, CrcDetailSerializer, TransitDetailSerializer
from users.serializers import UserSerializer

from .models import Request


class RequestSerializer(serializers.ModelSerializer):
    """
    Serializador para las solicitudes
    """

    crc = CrcDetailSerializer(many=False, read_only=True, required=False)
    cea = CeaDetailSerializer(many=False, read_only=True, required=False)
    transit = TransitDetailSerializer(many=False, read_only=True, required=False)
    related_tramits = serializers.StringRelatedField(many=True)
    request_date = serializers.DateTimeField(format="%d %B, %y - %I:%M %p")
    payment_date = serializers.DateTimeField(format="%d %B, %y - %I:%M %p")
    credit_status = serializers.SerializerMethodField()
    payment_type = serializers.SerializerMethodField()

    user = UserSerializer(many=False,)

    class Meta:
        model = Request
        fields = (
            'id', 'user', 'cea', 'crc', 'transit', 'payment_type',
            'total_price', 'crc_status', 'cea_status', 'request_status',
            'credit_status', 'credit_request_code', 'booking', 'request_date',
            'payment_date', 'payment_status', 'related_tramits'
        )

    def get_credit_status(self, obj):
        return obj.get_credit_status_display()

    def get_payment_type(self, obj):
        return obj.get_payment_type_display()

