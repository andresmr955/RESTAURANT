from drf_spectacular.utils import extend_schema
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action

from .serializers import AttendanceSerializer
from .models import Attendance
from datetime import datetime


@extend_schema(tags=["Attendance"])
class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]


    @action(detail=False, methods=['POST'], url_path='mark-entry')
    def mark_entry(self, request):
        user = request.user

        if Attendance.objects.filter(assigned_employee=user, login_end=None).exists():
            return Response({'error': 'You already have an open entry'}, status=status.HTTP_400_BAD_REQUEST)

        attendance = Attendance.objects.create(
            assigned_employee=user,
            login_start=None
        )

        attendance.login_start = datetime.now()
        attendance.save()
        return Response({'status': 'Saved entry time', 'login_start': attendance.login_start})

    @action(detail=False, methods=['POST'], url_path='mark-exit')
    def mark_exit(self, request, pk=None):
        """
        Marks the end time of the specified Attendance.
        """
        user = request.user

        try:
            attendance = Attendance.objects.get(assigned_employee=user, login_end=None)
        except Attendance.DoesNotExist:
            return Response({'error': 'You cant find an unlocked start'}, 
                            status=status.HTTP_400_BAD_REQUEST)

        attendance.login_end = datetime.now()
        attendance.save()
        return Response({'status': 'Saved output log'})

    @action(detail=False, url_path='user/(?P<user_id>[^/.]+)')
    def attendances_by_user(self, request, user_id=None):
        attendances = self.queryset.filter(assigned_employee_id=user_id)
        serializer = self.get_serializer(attendances, many=True)
        
        return Response(serializer.data)