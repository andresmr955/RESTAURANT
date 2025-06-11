from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    EmployeeCreateView, 
    EmployeeList, 
    CustomLoginView,
    LoginView,
    EmployeeListAPI

    )

from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'users'

urlpatterns = [
   
   
    # path('login/', CustomLoginView.as_view(template_name="users/login.html") , name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page="users:login"), name="logout"),
    path('add-employee/', EmployeeCreateView.as_view(), name="add-employee"),
    path('employee-list/', EmployeeList.as_view(), name="employee_list" ),
    path("loginjwt/",   LoginView.as_view(),     name="jwt_login"),   # POST
    path("refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    path("employees-list-api", EmployeeListAPI.as_view(), name="api_employees_list")
]