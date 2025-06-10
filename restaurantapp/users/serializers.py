from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        # Añadir info extra al payload:
        token["username"] = user.username
        token["email"] = user.email
        token["is_manager"] = user.is_manager()
        return token