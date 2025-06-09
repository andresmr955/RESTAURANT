from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    EmployeeCreateView, 
    EmployeeList, 
    DashboardAdminView,
    )

app_name = 'users'

urlpatterns = [
   
    # Agrega aquí tus rutas de usuario
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html") , name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page="login"), name="logout"),
    path('add-employee/', EmployeeCreateView.as_view(), name="add-employee"),
    path('employee-list/', EmployeeList.as_view(), name="employee-list" ),
    path('admin_dashboard/', DashboardAdminView.as_view(), name="admin-dashboard" )
]