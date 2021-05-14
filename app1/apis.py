import json
from json import JSONDecodeError
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db import IntegrityError
from django.db.models import ProtectedError
from . import models
from .models import Class, Student
from .data_factory import response_dict, JR


# 班级管理
def manage_class(request):
    # 增加班级
    if request.method == 'POST':
        try:
            name = json.loads(request.body)['name']
            c = Class(name=name)
            c.save()
            return JR(response_dict(code=0, msg='添加成功'))
        except (JSONDecodeError, KeyError, TypeError):
            return JR(response_dict(code=500, msg='参数错误', success=False))
        except IntegrityError:
            return JR(response_dict(code=300, msg='班级已存在', success=False))

    # 删除班级
    elif request.method == 'DELETE':
        try:
            class_id = request.GET.get('id')
            assert class_id is not None
            result = Class.objects.filter(id=class_id).delete()
            if result[0] == 0:
                return JR(response_dict(code=100, msg='班级不存在', success=False))
            elif result[0] == 1:
                return JR(response_dict(code=0, msg='删除成功'))
        except ProtectedError as e:
            if 'Student' in str(e):
                return JR(response_dict(code=400, msg='该班级下存在学生，不可删除', success=False))
        except (ValueError, AssertionError):
            return JR(response_dict(code=500, msg='参数错误', success=False))

    # 更新班级
    elif request.method == 'PUT':
        try:
            json_data = json.loads(request.body)
            class_id = json_data['id']
            name = json_data['name']
            result = Class.objects.filter(id=class_id).update(name=name)
            if result == 1:
                return JR(response_dict(code=0, msg='修改成功'))
            elif result == 0:
                return JR(response_dict(code=100, msg='班级不存在', success=False))
        except (JSONDecodeError, KeyError, TypeError):
            return JR(response_dict(code=500, msg='参数错误', success=False))
        except IntegrityError:
            return JR(response_dict(code=300, msg='班级已存在', success=False))

    # 查询班级
    elif request.method == 'GET':
        try:
            if not request.GET.get('page'):
                page = 1
            else:
                page = request.GET.get('page')

            if not request.GET.get('pagesize'):
                pagesize = 10
            else:
                pagesize = request.GET.get('pagesize')

            data = {}
            result = models.Class.objects.all().order_by('id')
            paginator = Paginator(result, pagesize)
            class_list = []
            try:
                rs = serializers.serialize('python', paginator.page(page))
                for r in rs:
                    class_list.append(r['fields'])
            except EmptyPage:
                pass
            data['list'] = class_list
            data['currPage'] = page
            data['pagesize'] = pagesize
            data['totalCount'] = result.count()
            data['totalPage'] = paginator.num_pages
            return JR(response_dict(code=0, msg='查询成功', data=data))
        except (ZeroDivisionError, ValueError, PageNotAnInteger, AssertionError):
            return JR(response_dict(code=500, msg='参数错误', success=False))