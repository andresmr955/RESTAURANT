from django.contrib import admin
from .models import Task

# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('assigned_employee','id', 'status', 'description', 'priority', 'assigned_date')
    search_fields = ('description', 'assigned_employee__email')
    list_filter = ('status', 'priority', 'assigned_date')
    ordering = ('assigned_date',)