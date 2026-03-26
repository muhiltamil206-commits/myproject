from django.contrib import admin

# Register your models here.

from .models import AppointmentModel

admin.site.register(AppointmentModel)
