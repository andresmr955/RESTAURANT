from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    EmployeeCreateView, 
    EmployeeList, 
    CustomLoginView,
    LoginView,
    EmployeeListAPI,
    EmployeeCreateAPI

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
    path("employees-list/", EmployeeListAPI.as_view(), name="employees_list_api"),
    # http://127.0.0.1:8000/api/auth/employees-list-api
    path("add-employee-api/", EmployeeCreateAPI.as_view(), name="add_employee_api")
    #http://localhost:8000/api/auth/add-employee-api/
]