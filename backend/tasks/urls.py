from django.contrib import admin
from django.urls import path, include
from django.conf import settings    
from django.conf.urls.static import static
from .views import TaskCreateView, TaskListView, TaskDetailView, EmployeeTaskListView
from .viewsets import TaskViewSet

from rest_framework.routers import DefaultRouter

app_name = 'tasks'

router = DefaultRouter()
router.register("tasks", TaskViewSet) 

urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='create_task'),
    path('tasks-html/', TaskListView.as_view(), name='task_list'),
    path('task-detail/<int:pk>', TaskDetailView.as_view(), name='task_detail'),
    path('employee/<int:employee_id>/', EmployeeTaskListView.as_view(), name='task_list'),
  
] + router.urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)