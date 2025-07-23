from django.contrib.auth import authenticate

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import exceptions, serializers

from users.models import CustomerUser

class CustomTokenSerializer(TokenObtainPairSerializer):
    username = None

    @classmethod
    def get_token(cls, user):
        # Gets the base token and adds additional information to the payload
        token = super().get_token(user)
        token["username"] = user.username  # Include the 'username' in the token
        token["email"] = user.email  # Include the email in the token
        token["is_manager"] = user.is_manager()  # Add other relevant fields if necessary
        token["is_chef"] = user.is_chef()  
        token["is_cook"] = user.is_cook()  
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