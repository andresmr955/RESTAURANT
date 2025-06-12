from django.contrib.auth import authenticate
from rest_framework import exceptions
from .models import CustomerUser
from rest_framework import serializers



class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = [  'role',
                    'phone_number',
                    'avatar',
                    'date_birth',
                    'address',
                    'notifications_enabled',
                    'date_joined_restaurant',
                    'average_task_completed']

class EmployeeCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerUser
        fields = [  'email',
                    'role',
                    'phone_number',
                    'avatar',
                    'date_birth',
                    'address',
                    'notifications_enabled',
                    'date_joined_restaurant',
                    'average_task_completed']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        # Use create_user if you have a method that handles password hashing
        validated_data['username'] = validated_data['email'].split('@')[0]

        user = CustomerUser.objects.create_user(**validated_data)
        return user