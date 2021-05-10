import json

from django.core import serializers
from django.http import JsonResponse
from . import models
from .models import Class


def find_all(request):
    r = models.Student.objects.all()
    students = serializers.serialize('python', r)
    list_data = []
    for s in students:
        list_data.append(s['fields'])
    json_data = {'code': 0, 'msg': '查询成功', 'data': list_data}
    return JsonResponse(json_data, json_dumps_params={"ensure_ascii": False})


def add_class(request):
    if request.method == 'POST':
        if request.body:
            name = json.loads(request.body)['name']
            c = Class(name=name)
            a = c.save()
            print(a)
            return JsonResponse({'code': 0, 'msg': '添加成功', 'data': ''}, json_dumps_params={"ensure_ascii": False})
        return JsonResponse({'code': 500, 'msg': '参数错误', 'data': ''}, json_dumps_params={"ensure_ascii": False})
