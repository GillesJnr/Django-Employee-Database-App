from django.shortcuts import render, redirect
from . forms import EmployeeForm

# Create your views here.


def employee_form(request):
    form = EmployeeForm()
    return render(request, "employees/employee_form.html", {'form': form})


def employee_list(request):
    return render(request, "employees/employee_list.html")


def employee_delete(request):
    return