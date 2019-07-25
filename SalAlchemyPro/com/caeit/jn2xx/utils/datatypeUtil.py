# -*- coding: utf-8 -*-


__author__ = 'Eugene Gao'
__date__ = '2018.08.13'


def strWrappedQuota(st):
    return "'" + st + "'" if isinstance(st, str) else str(st)


def str2Utf8Byte(st):
    return bytes(str(st), encoding='utf-8')


if __name__ == '__main__':
    strList = ["a", 2, "hello", "*"]
    print(strWrappedQuota(strList[1]))
    print(str2Utf8Byte(strList[1]))