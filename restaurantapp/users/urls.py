from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    EmployeeCreateView, 
    EmployeeList, 
    CustomLoginView,
    LoginView,
    EmployeeListCreateAPI, 
    EmployeeDetailUpdateAPI

    )

from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'users'

urlpatterns = [
   
    #URLS TO PROVE MY MODELS
    path('login/', CustomLoginView.as_view(template_name="users/login.html") , name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page="users:login"), name="logout"),
    path('add-employee/', EmployeeCreateView.as_view(), name="add-employee"),
    path('employee-list/', EmployeeList.as_view(), name="employee_list" ),
    


    ##APIS FOR MY FRONTEND
    
    path("loginjwt/",   LoginView.as_view(),  name="jwt_login"),   # POST
    # http://127.0.0.1:8000/api/auth/loginjwt/
    path("refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    # http://127.0.0.1:8000/api/auth/refresh/
    path("employees/", EmployeeListCreateAPI.as_view(), name="employees_api"),
    # http://127.0.0.1:8000/api/auth/employees/
    path('employees/<int:pk>/', EmployeeDetailUpdateAPI.as_view(), name='employee-detail-update')
    # http://127.0.0.1:8000/api/auth/employees/employees/<int:id>/

  
]