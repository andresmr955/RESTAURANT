from django.urls import path
from .views import HomeView, DashboardAdminView

app_name = 'core'

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('admin-dashboard/', DashboardAdminView.as_view(), name="admin_dashboard" )
]