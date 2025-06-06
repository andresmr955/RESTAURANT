from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
# class Restaurant(models.Model):
#     nombre = models.CharField(max_length=100)

# class Employee(AbstractUser):
#     restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
#     entry_hour = models.TimeField()
#     exit_hour = models.TimeField()

class CustomerUser(AbstractUser):
    ROLE_CHOICES = [
        ('admin', 'Manager'),
        ('chef', 'Sous chef'), 
        ('cook', 'Cook')
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='cook')

    def __str__(self):
        return f"{self.username} ({self.get_role_display()})" 