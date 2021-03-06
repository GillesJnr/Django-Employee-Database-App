from django.db import models


# Create your models here.


class Position(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class Employee(models.Model):
    employee_name = models.CharField(max_length=250, unique=True)
    address = models.CharField(max_length=100)
    employment_code = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10)
    position = models.ForeignKey('Position', on_delete=models.CASCADE)

    def __str__(self):
        return self.employee_name
