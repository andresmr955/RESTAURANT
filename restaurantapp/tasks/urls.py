from django.contrib import admin
from django.urls import path, include
from django.conf import settings    
from django.conf.urls.static import static
from .views import TaskCreateView, TaskListView, TaskDetailView

app_name = 'tasks'

urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='create_task'),
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('task-detail/<int:pk>', TaskDetailView.as_view(), name='task_detail')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)