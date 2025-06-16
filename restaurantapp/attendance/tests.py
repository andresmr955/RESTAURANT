from datetime import datetime, timedelta
from django.test import TestCase
from .models import Attendance
from users.models import CustomerUser

class AttendanceModelTest(TestCase):
    def setUp(self):
        # Creamos un usuario de prueba
        self.user = CustomerUser.objects.create_user(username='testuser', password='secret')

        # Creamos una asistencia de prueba
        self.attendance = Attendance.objects.create(
            assigned_employee = self.user,
            date_login = datetime(2025, 6, 16).date(), 
            login_start = datetime(2025, 6, 16, 8, 0), 
            login_end = datetime(2025, 6, 16, 16, 0)
        )

    def test_total_horas(self):
        """Prueba que total_horas calcule correctamente el total de horas trabajadas."""
        self.attendance.login_start = datetime(2025, 6, 16, 8, 0)
        self.attendance.login_end = datetime(2025, 6, 16, 16, 0)
        self.attendance.save()

        hours = self.attendance.total_hours()
        self.assertEqual(hours, 8)
