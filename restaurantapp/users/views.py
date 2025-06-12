from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import UserPassesTestMixin


from rest_framework.generics import ( ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from drf_spectacular.utils import extend_schema

from .models import CustomerUser
from .serializers import EmployeeSerializer, EmployeeCreateSerializer
from .forms import EmployeeForm


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




class EmployeeList(UserPassesTestMixin, ListView):
    model = CustomerUser
    template_name = 'users/employee_list.html'
    context_object_name = 'employees'

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_manager()
    
    def get_queryset(self):
        return CustomerUser.objects.exclude(role='admin')

@extend_schema(tags=["Users"])
class EmployeeListCreateAPI(ListCreateAPIView):
    """
    Get the list of employees or create employees
    """
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

@extend_schema(tags=["Users"])
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