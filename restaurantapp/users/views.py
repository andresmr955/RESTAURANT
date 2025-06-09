from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import UserPassesTestMixin
from .models import CustomerUser
from .forms import EmployeeForm


class EmployeeCreateView(UserPassesTestMixin, CreateView):
    model = CustomerUser
    form_class = EmployeeForm
    template_name = 'users/add_employee.html'
    success_url = reverse_lazy('employee_list')

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_manager()

class EmployeeList(UserPassesTestMixin, ListView):
    model = CustomerUser
    template_name = 'users/employee_list.html'
    context_object_name = 'employees'

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_manager()
    
    def get_queryset(self):
        return CustomerUser.objects.exclude(role='admin')