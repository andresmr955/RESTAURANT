# tasks/views.py
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, ListView, DetailView

from django.utils import timezone
from django.shortcuts import redirect
from rest_framework import status

from users.models import CustomerUser
from .models import Task
from .forms import TaskForm
from .serializers import TaskSerializer

class TaskCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create_task.html'
    success_url = reverse_lazy('tasks:create_task')  
   
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (user.is_manager() or user.is_chef())

    def form_valid(self, form):
        return super().form_valid(form)


class TaskListView(ListView):

    model = Task
    template_name = 'tasks/task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(assigned_employee=user)

class TaskDetailView(DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'

    def post(self, request, *args, **kwargs):
        task = self.get_object()
        action = request.POST.get('action')

        if action == 'start' and not task.start_time:
            task.start_time = timezone.now()
            task.save()
        elif action == 'stop' and task.start_time and not task.end_time:
            task.status = "completed"
            task.end_time = timezone.now()
            task.save()

        return redirect(reverse_lazy('tasks:task_detail', kwargs={'pk': task.pk}))

class EmployeeTaskListView(ListView):
    model = Task
    template_name = 'tasks/employee_task_list.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        employee_id = self.kwargs['employee_id']
        return Task.objects.filter(assigned_employee__id=employee_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employee'] = CustomerUser.objects.get(id=self.kwargs['employee_id'])
        return context

