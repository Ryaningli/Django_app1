from django.contrib import admin
from .models import Class, Subject, Teacher, Student

# Register your models here.


# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('id', 'name', 'gender', 'birthday', 'fraction', 's_class_id')

admin.site.register([Class, Subject, Teacher, Student])
