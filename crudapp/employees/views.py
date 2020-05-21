from django.shortcuts import render, redirect
from . forms import EmployeeForm
from . models import Employee

# Create your views here.


def employee_list(request):
    employee_data = Employee.objects.all()
    # list_xs = {employee_data}
    list_result = [entry for entry in employee_data]  # converts ValuesQuerySet into Python list
    context = {"list_result": list_result}
    # print(context)
    return render(request, "employees/employee_list.html", context)


def employee_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            employee = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=employee)
        return render(request, "employees/employee_form.html", {'form': form})

    else:
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('list')


def employee_delete(request):
    return