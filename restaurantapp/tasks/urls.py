from django.contrib import admin
from django.urls import path, include
from django.conf import settings    
from django.conf.urls.static import static
from .views import TaskCreateView

app_name = 'tasks'

urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='create_task')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)