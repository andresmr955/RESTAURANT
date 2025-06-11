from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from .forms import EmployeeForm

from django.http import HttpResponseBadRequest


from rest_framework_simplejwt.views import TokenObtainPairView

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status



##  Important Imports
from rest_framework.generics import (
    ListCreateAPIView, 
    RetrieveUpdateAPIView, 
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import CustomerUser
from .serializers import CustomTokenSerializer, EmployeeSerializer, EmployeeCreateSerializer



class CustomLoginView(LoginView):
    template_name = 'users/login.html'

    def get_success_url(self):
        user = self.request.user
        if user.is_manager():
            return reverse_lazy('core:admin_dashboard')
        else: 
            return reverse_lazy('tasks:task_list')
            
class EmployeeCreateView(UserPassesTestMixin, CreateView):
    model = CustomerUser
    form_class = EmployeeForm
    template_name = 'users/add_employee.html'
    success_url = reverse_lazy('users:employee_list')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_manager()

    def form_invalid(self, form):
        print(form.errors)  # Imprime los errores en consola para depuración
        return super().form_invalid(form)



class LoginView(TokenObtainPairView):
    serializer_class = CustomTokenSerializer

    def post(self, request, *args, **kwargs):
        # Verificar los datos recibidos en el request
        print("Datos del request:", request.data)
        print("Datos recibidos del serializer:", request.data.get('email'), request.data.get('password'))

        # Pasar los datos al serializer y validar
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.validated_data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeList(UserPassesTestMixin, ListView):
    model = CustomerUser
    template_name = 'users/employee_list.html'
    context_object_name = 'employees'

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_manager()
    
    def get_queryset(self):
        return CustomerUser.objects.exclude(role='admin')


class EmployeeListCreateAPI(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = CustomerUser.objects.all()

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return EmployeeCreateSerializer
        return EmployeeSerializer

    def perform_create(self, serializer):
        if not self.request.user.is_manager():
            raise PermissionDenied("Only managers can create employees")
        serializer.save()

class EmployeeDetailUpdateAPI(RetrieveUpdateDestroyAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk' 

    def get_queryset(self):
        user = self.request.user
        if user.is_manager():
            return CustomerUser.objects.all()
        return CustomerUser.objects.none()

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_manager():
            raise PermissionDenied("Just managers can delete employees")
        return super().destroy(request, *args, **kwargs)