from django.urls import path
from rest_framework.routers import DefaultRouter
from .viewsets import AttendanceViewSet

app_name = 'attendance' 

router = DefaultRouter()
router.register(r'attendance', AttendanceViewSet, basename='attendance')

urlpatterns = [
    
] + router.urls