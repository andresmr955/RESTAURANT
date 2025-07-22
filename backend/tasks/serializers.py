# tasks/serializers.py
from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'status', 'description', 'assigned_employee', 'priority', 'assigned_date', 'start_time', 'end_time', 'comments']
