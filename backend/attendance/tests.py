from datetime import datetime, timedelta
from django.test import TestCase
from .models import Attendance
from users.models import CustomerUser

class AttendanceModelTest(TestCase):
    def setUp(self):
        # We create a test user
        self.user = CustomerUser.objects.create_user(username='testuser', password='secret')

        # We create a test assistance
        self.attendance = Attendance.objects.create(
            assigned_employee = self.user,
            date_login = datetime(2025, 6, 16).date(), 
            login_start = datetime(2025, 6, 16, 8, 0), 
            login_end = datetime(2025, 6, 16, 16, 0)
        )

    def test_total_horas(self):
        """Test that total_hours correctly calculates the total hours worked"""
        self.attendance.login_start = datetime(2025, 6, 16, 8, 0)
        self.attendance.login_end = datetime(2025, 6, 16, 16, 0)
        self.attendance.save()

        hours = self.attendance.total_hours()
        self.assertEqual(hours, 8)
