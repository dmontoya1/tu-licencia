# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

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


class UserCustomSerializer(serializers.ModelSerializer):
	"""Serializador para el model de Usuario
	"""

	email = serializers.EmailField(validators=[
		UniqueValidator(
			queryset=get_user_model().objects.all(),
			message="Ya existe un usuario con este email",
		)]
	)

	class Meta:
		model = get_user_model()
		fields = ('email', 'username')

	
	def update(self, instance, validated_data):
		instance.email = validated_data['email']
		instance.username = validated_data['document_id']
		try:
			customer = instance.customer_profile
			customer.email = validated_data['email']
			customer.save()
		except Exception as e:
			print ("Exception")
			print (e)
		instance.save()
		return instance
