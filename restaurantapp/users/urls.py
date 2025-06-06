from django.urls import path
from django.contrib.auth import view as auth_views
from . import views

app_name = 'users'

urlpatterns = [
   
    # Agrega aquí tus rutas de usuario
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html")),
    path('logout/', auth_views.LogoutView.as_view(next_page="/"), name="logout")
]