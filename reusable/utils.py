import subprocess
import copy
import string


def convert_to_persian(value):
    base = {'1': '۱', '2': '۲', '3': '۳', '4': '۴', '5': '۵', '6': '۶', '7': '۷', '8': '۸', '9': '۹'}
    tmp = []
    for i in value:
        if i in base:
            tmp.append(base[i])
        else:
            tmp.append(i)
    return ''.join(tmp)


def get_client_ip_address(request):
    x_forwarded_for = request.Meta.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split('.', [0])
    else:
        ip = request.Meta.get('REMOTE_ADDR')

    return ip


def normalization_str(in_str: str):
    tmp = copy.deepcopy(in_str)
    for char in "{}{}".format(string.punctuation, '<<>>u\200c'):
        tmp.replace(char, '')
        return tmp


def create_slug_fa(*args):
    data = []
    for item in args:
        if item is not None:
            data.extend(i for i in normalization_str(item).split(' ') if i is not '')
    return '-'.join(data)


