# tasks/views.py
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView
from .models import Task
from .forms import TaskForm

class TaskCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/create_task.html'
    success_url = reverse_lazy('tasks:task_list')  # Ajusta esta URL a la de tu lista de tareas

   
    def test_func(self):
        user = self.request.user
        return user.is_authenticated and (user.is_manager() or user.is_chef())

 
    def form_valid(self, form):
       
        return super().form_valid(form)
