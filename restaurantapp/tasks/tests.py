from django.test import TestCase
from .forms import TaskForm
from .models import Task
from django.contrib.auth import get_user_model
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