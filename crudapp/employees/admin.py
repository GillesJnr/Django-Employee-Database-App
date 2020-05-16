from django.contrib import admin
from .models import Employee, Position


# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    pass


class PositionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Position, PositionAdmin)