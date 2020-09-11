#!/usr/bin/env python3
# -*- coding: utf-8 -*-



if __name__ == "__main__":
    # host=input("host&port:")
    host = "192.168.200.66:48081"
    path = r"/api/v1/addressable"
    url = "http://" + host + path
    print(url)
    type = "get"
