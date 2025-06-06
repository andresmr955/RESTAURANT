from django.db import models
from django.conf import settings
# Create your models here.


class Attendance(models.Model):
    assigned_employee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='attendances')
    date_login = models.DateField(auto_now_add=True)
    login_start = models.DateField(blank=True, null=True)
    login_end = models.DateField(blank=True, null=True)


    def total_horas(self):
            if self.login_start and self.login_start:
                return (self.login_start - self.login_start).total_seconds() / 3600
            return 0

    def __str__(self):
        return f"Attendance of {self.assigned_employee.username} on {self.date_login}"