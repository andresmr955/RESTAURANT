from django.db import models
from django.conf import settings
from datetime import timedelta

# Create your models here.

class Task(models.Model):

    STATUS_CHOICES = [
            ('pending', 'Pending'),
            ('in progress', 'In Progress'), 
            ('completed', 'Completed')
        ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default = 'pending')
    description = models.CharField(max_length=255)
    assigned_employee = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, 
        related_name = 'tasks'
    )
    priority = models.IntegerField(default=1)
    assigned_date = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    comments = models.TextField(blank=True, null=True)

    def total_time_minutes(self):
        if self.start_time and self.end_time:
            return round((self.end_time - self.start_time).total_seconds() / 60, 2)
        return None

    @property
    def duration(self):
        if self.start_time and self.end_time:
            return self.end_time - self.start_time
        return timedelta()
        
    def __str__(self):
        return f"{self.description} for {self.assigned_employee.username}"
    