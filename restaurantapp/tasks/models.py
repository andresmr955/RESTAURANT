from django.db import models
from django.conf import settings
# Create your models here.

class Task(models.Model):

    STATUS_CHOICES = [
            ('pending', 'Pending'),
            ('in progress', 'In Progress'), 
            ('completed', 'Completed')
        ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default = 'Pending')
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

    def total_time(self):
        if self.start_time and self.end_time:
            return (self.end_time - self.start_time) / 60
        return None

    def __str__(self):
        return f"{Self.description} for {self.assigned_employee.username}"
    