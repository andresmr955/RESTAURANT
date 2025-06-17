from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['assigned_employee', 'priority', 'status', 'description' ]