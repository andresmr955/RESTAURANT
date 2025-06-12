from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import exceptions
from .models import CustomerUser
from rest_framework import serializers

class CustomTokenSerializer(TokenObtainPairSerializer):
    username = None

    @classmethod
    def get_token(cls, user):
        # Gets the base token and adds additional information to the payload
        token = super().get_token(user)
        token["username"] = user.username  # Include the 'username' in the token
        token["email"] = user.email  # Include the email in the token
        token["is_manager"] = user.is_manager()  # Add other relevant fields if necessary
        return token

    def validate(self, attrs):
        email = attrs.get("email")  # We use 'email' here

        password = attrs.get("password")
        if not email:
            raise exceptions.AuthenticationFailed("Email is required")
        # Find the user by email
        try:
            user = CustomerUser.objects.get(email=email)  # Find the user by email
        except CustomerUser.DoesNotExist:
            raise exceptions.AuthenticationFailed("No user found with this email")

        # Perform authentication with 'username', as this is what Django uses by default
        user = authenticate(username=user.email, password=password)  # Use 'username' to authenticate
        if not user:
            raise exceptions.AuthenticationFailed("Invalid credentials")

        # If everything is okay, we generate the token
        return super().validate(attrs)

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