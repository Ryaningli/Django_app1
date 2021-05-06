from django.core import serializers
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render
from . import models


def index(request):
    context = {}
    r = models.Student.objects.all()
    students = serializers.serialize('python', r)
    context['jsonData'] = students
    return render(request, 'index.html', context)
