from django.contrib import admin
from .models import Class, Subject, Teacher, Student

# Register your models here.

admin.site.register([Class, Subject, Teacher, Student])
