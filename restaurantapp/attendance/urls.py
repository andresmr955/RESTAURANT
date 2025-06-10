from django.urls import path
from .views import HelloWorld, start_attendance, stop_attendance, attendance_page
app_name = 'attendance' 

urlpatterns = [
    path('start/', start_attendance, name='start_attendance'),
    path('stop/', stop_attendance, name='stop_attendance'),
    path('', attendance_page, name='attendance_page'),
     path('api/hello/', HelloWorld.as_view(), name='hello_world')
]