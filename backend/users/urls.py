from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    EmployeeCreateView, 
    EmployeeList,
    )

from .viewsets import EmployeeViewSet

app_name = 'users'

router = DefaultRouter()
router.register(r'employees-actions', EmployeeViewSet, basename='employees')

urlpatterns = [

        #URLS TO PROVE MY MODELS
    path('add-employee/', EmployeeCreateView.as_view(), name="add-employee"),
    path('employee-list/', EmployeeList.as_view(), name="employee_list" ),

 
] + router.urls