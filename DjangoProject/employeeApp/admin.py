from django.contrib import admin

# Register your models here.

from .models import employeeModel

admin.site.register(employeeModel)