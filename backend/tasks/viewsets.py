from rest_framework import viewsets, permissions
from rest_framework.exceptions import PermissionDenied
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone

from .serializers import TaskSerializer
from .models import Task

@extend_schema(tags=["Tasks"])
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated] 

    def perform_create(self, serializer):
        """
            Here we can implement that only the manager can create tasks.

        """
        if not self.request.user.is_manager():
            raise PermissionDenied("Only managers can create employees")
        serializer.save()

    def get_queryset(self):
        queryset = Task.objects.all()
        assigned_employee = self.request.query_params.get('assigned_employee')
        if assigned_employee:
            queryset = queryset.filter(assigned_employee=assigned_employee)
        return queryset

    @action(detail=True, methods=['post'])
    def start(self, request, pk=None):
        task = self.get_object()
        if not task.start_time:
            task.start_time = timezone.now()
            task.save()
        return Response({'status': 'started'})


    @action(detail=True, methods=['post'])
    def stop(self, request, pk=None):
        task = self.get_object()
        if task.start_time and not task.end_time:
            task.end_time = timezone.now()
            task.save()
        return Response({'status': 'stopped'})

    
    