from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import exceptions
from .models import CustomerUser
from rest_framework import serializers

class CustomTokenSerializer(TokenObtainPairSerializer):
    username = None

    @classmethod
    def get_token(cls, user):
        # Obtiene el token base y agrega información adicional al payload
        token = super().get_token(user)
        token["username"] = user.username  # Incluir el 'username' en el token
        token["email"] = user.email  # Incluir el email en el token
        token["is_manager"] = user.is_manager()  # Agregar otros campos relevantes si es necesario
        return token

    def validate(self, attrs):
        email = attrs.get("email")  # Usamos 'email' aquí

        password = attrs.get("password")
        if not email:
           raise exceptions.AuthenticationFailed("Email is required")
        # Buscar al usuario por email
        try:
            user = CustomerUser.objects.get(email=email)  # Buscar al usuario por email
        except CustomerUser.DoesNotExist:
            raise exceptions.AuthenticationFailed("No user found with this email")

        # Realizar autenticación con 'username', ya que es lo que usa Django por defecto
        user = authenticate(username=user.email, password=password)  # Usar 'username' para autenticar
        if not user:
            raise exceptions.AuthenticationFailed("Invalid credentials")

        # Si todo está bien, generamos el token
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

