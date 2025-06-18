from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    LoginView,
    CustomLoginView,
    

    )

from rest_framework_simplejwt.views import TokenRefreshView


app_name = 'my_auth'

urlpatterns = [
   
    #URLS TO PROVE MY MODELS
    path('login/', CustomLoginView.as_view(template_name="my_auth/login.html") , name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page="my_auth:login"), name="logout"),
  
        ##APIS FOR MY FRONTEND
    path("loginjwt/", LoginView.as_view(),  name="jwt_login"),   # POST
    # http://127.0.0.1:8000/api/auth/loginjwt/
    path("refresh/", TokenRefreshView.as_view(), name="jwt_refresh"),
    # http://127.0.0.1:8000/api/auth/refresh/
]