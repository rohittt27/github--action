from django.test import TestCase
from django.urls import reverse
from .models import Employee

class EmployeeAPITests(TestCase):
    def test_create_employee_api(self):
        url = reverse('employee_create')
        data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com',
            'department': 'IT',
            'designation': 'Developer'
        }
        response = self.client.post(url, data)
        self.assertEqual(Employee.objects.count(), 1)
        employee = Employee.objects.first()
        self.assertEqual(employee.name, 'John Doe')
        self.assertEqual(employee.email, 'john.doe@example.com')
        self.assertEqual(employee.department, 'IT')
        self.assertEqual(employee.designation, 'Developer')
