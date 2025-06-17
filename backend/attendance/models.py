from django.db import models
from django.conf import settings
from django.utils import timezone
# Create your models here.


class Attendance(models.Model):
    assigned_employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='attendances')
    date_login = models.DateField(auto_now_add=True)
    login_start = models.DateTimeField(blank=True, null=True)
    login_end = models.DateTimeField(blank=True, null=True)


    def total_hours(self):
        if self.login_start and self.login_end:
              # Ensure that both are timezone aware
            start = self.login_start
            end = self.login_end
            if timezone.is_naive(start):
                start = timezone.make_aware(start, timezone.get_current_timezone())
            if timezone.is_naive(end):
                end = timezone.make_aware(end, timezone.get_current_timezone())

            diff = end - start
            return diff.total_seconds() / 3600
        return 0

    def __str__(self):
        return f"Attendance of {self.assigned_employee.username} on {self.date_login}"