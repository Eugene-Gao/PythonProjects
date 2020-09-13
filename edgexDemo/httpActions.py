#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import requests


def get(url):
    res = requests.get(url)
    result = res.text
    return result


def post(url, querystr):
    data = eval(querystr)
    res = requests.post(url, data=data)
    result = res.text
    return result


def put(url, querystr):
    if querystr != None and querystr != "":
        data = eval(querystr)
        res = requests.put(url, data=data)
        result = res.text
        print(result)
    res = requests.put(url)
    result = res.text
    return result


def delete(url, querystr):
    res = requests.delete(url)
    result = res.text
    return result

if __name__ == "__main__":
    # host=input("host&port:")
    host = "192.168.200.66:48081"
    path = r"/api/v1/addressable"
    url = "http://" + host + path
    print(url)
    type = "get"

    str = ""
    with open("querystr.txt") as f:
        str = f.read().strip()

    if type == "get":
        get(url)
    elif type == "post":
        post(url, str)
    elif type == "put":
        put(url, str)
    elif type == "delete":
        delete(url, str)
