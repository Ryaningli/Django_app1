def response_dict(code=0, msg="", success=True, data=None, **kw):
    d = {'code': code, 'msg': msg, 'success': success, 'data': data}
    for k, v in kw.items():
        d[k] = v
    return d


if __name__ == '__main__':
    print(response_dict(500, "处理失败", False, {'test': 1}))