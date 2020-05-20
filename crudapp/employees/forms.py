from .models import Employee
from django import forms


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ('employee_name', 'address', 'phone_number', 'employment_code', 'position')
        labels = {
            'Employee name': 'Employee Name',
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label = 'Select Position'
        self.fields['employment_code'].required = False


