# -*- coding: utf-8 -*-
import json
from functools import reduce

__author__ = 'Eugene Gao'
__date__ = '2018.08.13'

import binascii


def strWrappedQuota(st):
    return "'" + st + "'" if isinstance(st, str) else str(st)


def str2Utf8Byte(st):
    return bytes(str(st), encoding='utf-8')


def str2Hex(bts):
    '''
    refer to function name
    :param bt: string
    :return: hex string
    '''
    return binascii.hexlify(bts.encode('utf8'))


def hex2Str(hexs):
    '''

    :param hexs: hex string
    :return: string
    '''
    return binascii.unhexlify(hexs).decode('utf8')


def jsonList2DictList(jsonList):
    '''
    jl = r'[{"name": "a", "email": "a@gmail.com"},{"name": "b", "email": "b@gmail.com"}]'
    print(type(jsonList2DictList(jl)))
    for do in jsonList2DictList(jl):
        print([k + '=' + v for k, v in do.items()])
    ===============================================================
    :param jsonList: a list is composed by some json strings
    :return: a list of dict objects
    '''
    return json.loads(jsonList)



if __name__ == '__main__':
    # strList = ["a", 2, "hello", "*"]
    # print(strWrappedQuota(strList[1]))
    # print(str2Utf8Byte(strList[3]))
    # str2Hex_slt_str = str2Hex(strList[2])
    # print(str2Hex_slt_str)
    # hex2Str_slt_str = hex2Str(str2Hex_slt_str)
    # print(hex2Str_slt_str)
    jl = r'[{"name": "a", "email": "a@gmail.com"},{"name": "b", "email": "b@gmail.com"}]'
    print(type(jsonList2DictList(jl)))
    for do in jsonList2DictList(jl):
        print([k + '=' + v for k, v in do.items()])

