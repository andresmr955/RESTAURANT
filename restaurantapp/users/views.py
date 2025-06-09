from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from .models import CustomerUser
from .forms import EmployeeForm

from django.http import HttpResponseBadRequest


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
    success_url = reverse_lazy('employee_list')

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


