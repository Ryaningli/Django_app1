from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse


def response_dict(code=0, msg="", success=True, data=None, **kw):
    d = {'code': code, 'msg': msg, 'success': success, 'data': data}
    for k, v in kw.items():
        d[k] = v
    return d


class JR(JsonResponse):
    def __init__(self, data, encoder=DjangoJSONEncoder, safe=True, json_dumps_params=None, **kwargs):
        if json_dumps_params is None:
            json_dumps_params = {'ensure_ascii': False}
        super().__init__(data, encoder, safe, json_dumps_params, **kwargs)


if __name__ == '__main__':
    print(response_dict(500, "处理失败", False, {'test': 1}))