from django.core import serializers
from django.shortcuts import render
from . import models


def index(request):
    context = {}
    r = models.Student.objects.all()
    students = serializers.serialize('python', r)
    context['jsonData'] = students
    return render(request, 'index.html', context)
