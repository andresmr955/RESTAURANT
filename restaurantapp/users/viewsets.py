from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, permissions, response
from rest_framework.decorators import action

from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response

from .models import CustomerUser
from .serializers import EmployeeSerializer, EmployeeCreateSerializer
from .permissions import IsManager
from tasks.serializers import TaskSerializer 

@extend_schema(tags=["Users"])
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ViewSet to take actions with employees:
    List, create, update, and delete

    """
    queryset = CustomerUser.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated, IsManager]
    lookupfield = 'pk'

    def get_serializer_class(self):
        if self.action == 'create':
            return EmployeeCreateSerializer
        return EmployeeSerializer

    def get_queryset(self):
        """
        Filter according to the users role that makes the consult
        """

        user = self.request.user
        if user.is_manager():
            return CustomerUser.objects.all().prefetch_related('tasks')
        return CustomerUser.objects.none()

    def perform_create(self, serializer):
        if not self.request.user.is_manager():
            raise PermissionDenied("Only managers can create employees")
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_manager():
            raise PermissionDenied("Just managers can delete employees")
        return super().destroy(request, *args, **kwargs)

    # Detail Action
    # URL: /api/users/{id}/send_notification/
    @action(methods=['POST'], detail=True, url_path=('set-on-notifications'))
    def send_on_notification(self, request, pk=None):
        """
        Activated a notification to a user in specific
        """ 
        user = self.get_object()
        user.notifications_enabled = True
        user.save()
        return response.Response({'status': f'User notification activated'})

    @action(methods=['POST'], detail=True, url_path=('set-off-notifications'))
    def send_off_notification(self, request, pk=None):
        """
        Deactivated a notification to a user in specific
        """ 
        user = self.get_object()
        user.notifications_enabled = False
        user.save()
        return response.Response({'status': f'User notification deactivated'})


    # Set Action 
    # URL: /api/users/send_notification_all/
    @action(methods=['POST'], detail=False, url_path=('set-on-notifications-all'))
    def send_on_notification_all(self, request):
        """
            Activations notifications to everyone
        """
        users = CustomerUser.objects.all()

        for user in users:
            user.notifications_enabled = True
            user.save()
        return response.Response({'status': f'Notifications activated all'})

    @action(methods=['POST'], detail=False, url_path=('set-off-notifications-all'))
    def send_off_notification_all(self, request):
        """
            Deactivation notifications to everyone
        """
        users = CustomerUser.objects.all()

        for user in users:
            user.notifications_enabled = False
            user.save()
        return response.Response({'status': f'Notifications deactivated all'})

    
    