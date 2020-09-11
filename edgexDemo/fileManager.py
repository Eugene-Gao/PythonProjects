#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import pathlib
import sys


class infoFile:


    def __init__(self, file):
        self.file = file

    # 获取文件属性
    def get_file_status(self):
        return os.stat(self.file)

    # 获取文件最近修改时间
    def get_getctime(self):
        return os.path.getctime(self.file)

    # 获取文件创建时间
    def get_getatime(self):
        return os.path.getatime(self.file)

    # 获取文件最近修改时间
    def get_getmtime(self):
        return os.path.getmtime(self.file)

    # 文件的字节尺寸
    def get_getsize(self):
        return os.path.getsize(self.file)

    # 返回当前工作目录
    def get_getcwd(self):
        return os.getcwd()

    # 路径的拼接和分离
    def split_join(self):
        Path = os.path.join(os.getcwd(), self.file)
        print(Path)  # 路径的拼接
        Path, filename = os.path.split(Path)
        print(Path, "和", filename)

    # 搜索模块的路径集，是一个list
    def get_syspath(self):
        return sys.path(self.file)

    # 获取当前系统编码
    def get_defaultencoding(self):
        return sys.getdefaultencoding(self.file)

    # 获取文件系统使用编码方式
    def get_filesystemencoding(self):
        return sys.getfilesystemencoding(self.file)


class wrfile:

    def __init__(self, file):
        self.file = file

    # 删除文件
    def del_file(self):
        if os.path.exists(self.file):  # 如果文件存在
            # 删除文件，可使用以下两种方法。
            os.remove(self.file)
            print("删除成功")
        # os.unlink(path)
        else:
            print('no such file:%s' % self.file)  # 则返回文件不存在

    # 文件写入
    def write_file(self):
        os.getcwd()
        mc = input("输入文件名")
        nr = input("输入内容")
        with open(file=mc, mode='w', buffering=-1) as f:
            f.write(nr)
        print("创建成功")

    # 创建文件夹
    def create_file(self):
        path = os.getcwd()
        name = input("name")
        os.mkdir(path + name)

    # 文件读取
    def rd_file(self):
        with open(self.file, 'r') as f:
            data = f.read()
            return data

    # 文件一行一行读取
    def rdplus_file(self):
        with open(self.file, 'r') as f:
            for eachline in f:
                print(eachline)

    # 重新命名
    def rename_file(self, newName):
        newName = input("加入新名字")
        os.rename(self.file, newName)

    # 编辑，在文字最后编辑
    def wrpuls_file(self, nr):
        with open(file=self.file, mode='a', buffering=-1) as f:
            f.write(nr)
        # print("成功")


if __name__ == '__main__':
    file_name = "querystr.txt"
    # if the file already exits, then delete the file firstly
    path = pathlib.Path(file_name)
    if path.exist() and path.is_file():
        os.remove(file_name)


    # create a new file with the same name
    file1 = infoFile(file_name)
    # check file status
    print(file1.get_file_status())#写入调用方法
    file2 = wrfile(file_name)
    # read the current file
    print(file2.wrpuls_file())
