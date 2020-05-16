from .models import Employee
from django import forms


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('employee_name', 'address', 'phone_number', 'employment_code', 'position')
        labels = {
            'Employee name': 'Employee Name',
        }
