from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Task

from .forms import TaskForm

from datetime import datetime, timedelta
from django.utils import timezone

# Create your tests here.

User = get_user_model()


class TaskFormTest(TestCase):
    def setUp(self):
        self.employee = User.objects.create_user(username='employee', password='testpass')
    
    def test_task_form_valid_data(self):
        form_data = {
            'description': 'Test task description',
            'assigned_employee': self.employee.id,
            'priority': 1, 
            'status': 'pending',

        }
        form = TaskForm(data=form_data)
        print(form_data)
        print(form.errors)
        self.assertTrue(form.is_valid())

    def test_task_form_missing_data(self):
        form_data = {
            'description': '',
            'assigned_employee': '',
            'priority': '',
            'status': '',
        }

        form = TaskForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors)
        self.assertIn('assigned_employee', form.errors)
        self.assertIn('priority', form.errors)
        self.assertIn('status', form.errors)

class TaskModelTest(TestCase):
    def setUp(self):
        self.employee = User.objects.create_user(username='employee', password='testpass')


    def test_task_creation(self):
        task = Task.objects.create(
            description='Test task',
            assigned_employee =self.employee,
            priority=1,
            status='pending'
        )

        self.assertEqual(task.description, 'Test task')
        self.assertEqual(task.status, 'pending')
        self.assertEqual(task.assigned_employee, self.employee)
        self.assertEqual(str(task), f"Test task for {self.employee.username}")

    def test_task_total_time_minutes(self):
        start_time = timezone.now()
        end_time = start_time + timedelta(hours=2)

        task = Task.objects.create(
            description= 'Task with time', 
            assigned_employee=self.employee, 
            priority=1,
            status="pending",
            start_time = start_time,
            end_time = end_time,
        )

        task.refresh_from_db()

        total_time = task.total_time_minutes()
        self.assertIsNotNone(total_time)
        self.assertAlmostEqual(total_time, 120, delta=1)
    
    def  test_task_total_time_returns_none_when_no_times(self):
        task = Task.objects.create(
            description= 'Task with no time', 
            assigned_employee=self.employee, 
            priority=1,
            status="pending",
        )

        self.assertIsNone(task.total_time_minutes())