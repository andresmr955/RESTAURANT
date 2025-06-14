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
        Marca la hora de inicio del Attendance especificado.
        """
        attendance = self.get_object()
        if attendance.entry_at is not None:
            return response.Response({'error': 'Ya tiene hora de inicio'}, 
                                      status=status.HTTP_400_BAD_REQUEST)

        attendance.entry_at = datetime.now()
        attendance.save()
        return response.Response({'status': 'Registro de inicio guardado'})
    

    @action(detail=True, methods=['POST'], url_path='mark-exit')
    def mark_exit(self, request, pk=None):
        """
        Marca la hora de fin del Attendance especificado.
        """
        attendance = self.get_object()
        if attendance.exit_at is not None:
            return response.Response({'error': 'Ya tiene hora de fin'}, 
                                      status=status.HTTP_400_BAD_REQUEST)

        attendance.exit_at = datetime.now()
        attendance.save()
        return response.Response({'status': 'Registro de salida guardado'})