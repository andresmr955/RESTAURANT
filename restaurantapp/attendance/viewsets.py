from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, permissions, response, status
from rest_framework.decorators import action

from .serializers import AttendanceSerializer
from .models import Attendance
from datetime import datetime


@extend_schema(tags=["Attendance"])
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]


    @action(detail=True, methods=['POST'], url_path='mark-entry')
    def mark_entry(self, request, pk=None):
        """
        Marks the start time of the specified Attendance.
        """
        attendance = self.get_object()
        if attendance.entry_at is not None:
            return response.Response({'error': 'Start time has already been set'}, 
                                      status=status.HTTP_400_BAD_REQUEST)

        attendance.entry_at = datetime.now()
        attendance.save()
        return response.Response({'status': 'Saved startup log'})
    

    @action(detail=True, methods=['POST'], url_path='mark-exit')
    def mark_exit(self, request, pk=None):
        """
        Marks the end time of the specified Attendance.
        """
        attendance = self.get_object()
        if attendance.exit_at is not None:
            return response.Response({'error': 'The end time is now'}, 
                                      status=status.HTTP_400_BAD_REQUEST)

        attendance.exit_at = datetime.now()
        attendance.save()
        return response.Response({'status': 'Saved output log'})