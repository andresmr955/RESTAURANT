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
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    date_birth = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    notifications_enabled = models.BooleanField(default=True)
    date_joined_restaurant = models.DateField(blank=True, null=True)
    average_task_completed = models.DateTimeField(blank=True, null=True)
    

    # Establecer email como campo de autenticación
    email = models.EmailField(unique=True)  # Aseguramos que el email sea único
    USERNAME_FIELD = 'email'  # Usamos 'email' como el campo de autenticación principal
    REQUIRED_FIELDS = ['username']  # username sigue siendo necesario para la creación del superusuario, pero no en la autenticación

    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})" 
    
    def is_manager(self):
        return self.role == 'admin'
    
    def is_chef(self):
        return self.role == 'chef'
    
    def is_cook(self):
        return self.role == 'cook'
    
    class Meta:
        ordering = ['username']