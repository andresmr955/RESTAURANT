from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status

from drf_spectacular.utils import extend_schema


from .serializers import CustomTokenSerializer
# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'my_auth/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_manager():
            return reverse_lazy('core:admin_dashboard')
        else:
            return reverse_lazy('tasks:task_list')


@extend_schema(tags=["UsersLogin"])
class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer

    def post(self, request, *args, **kwargs):
        # Verify the data received in the request
        print("Request Data:", request.data)
        print("Received data from serializer:", request.data.get('email'), request.data.get('password'))

        # Pass the data to the serializer and validate
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)