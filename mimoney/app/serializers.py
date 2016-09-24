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

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = (
            'name',
            'icon_mini'
        )

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Account
        fields = (
        	'user',
        	'balance'
        )

class MovementSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:
        model = models.Movement
        fields = (
            'category',
            'amount',
            'concept',
            'type',
            'contribution',
            'done',
            'date'
        )