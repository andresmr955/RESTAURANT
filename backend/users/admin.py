from django.contrib import admin
from .models import CustomerUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
@admin.register(CustomerUser)
class CustomerUserAdmin(UserAdmin):
    # I can customize according to my needs
    list_display = ('email', 'username', 'role', 'phone_number')
    search_fields = ('email', 'username')
    list_filter = ('role',)
    ordering = ('username',)