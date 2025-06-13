from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, permissions

from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied

from .models import CustomerUser
from .serializers import EmployeeSerializer, EmployeeCreateSerializer

@extend_schema(tags=["Users"])
class EmployeeViewSet(viewsets.ModelViewSet):
    """
    ViewSet to take actions with employees:
    List, create, update, and delete

    """
    queryset = CustomerUser.objects.all()
    permission_classes = [IsAuthenticated]
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
            return CustomerUser.objects.all()
        return CustomerUser.objects.none()

    def perform_create(self, serializer):
        if not self.request.user.is_manager():
            raise PermissionDenied("Only managers can crete employees")
        serializer.save()

    def destroy(self, request, *args, **kwargs):
        if not request.user.is_manager():
            raise PermissionDenied("Just managers can delete employees")
        return super().destroy(request, *args, **kwargs)