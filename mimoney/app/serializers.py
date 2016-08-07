from rest_framework import serializers
from django.contrib.auth.models import User
import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
        	'username',
        	'first_name',
        	'last_name',
        	'email'
        )

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = (
        	'user',
        	'balance'
        )