from django.contrib import admin
from .models import Patient, Doctor ,Todolist

# Register your models here.

admin.site.register(Patient)
admin.site.register(Doctor)