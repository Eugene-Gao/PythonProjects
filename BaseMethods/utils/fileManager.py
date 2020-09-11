#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
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
            return True
        # os.unlink(path)


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
    def rdTopBottom_file(self):
        with open(self.file, 'r', encoding='utf-8') as f:  # 打开文件
            lines = f.readlines()  # 读取所有行
            first_line = lines[0]  # 取第一行
            last_line = lines[-1]  # 取最后一行
            return first_line, last_line

    # 重新命名
    def rename_file(self, newName):
        os.rename(self.file, newName)

    # appending the new line on the bottom of the file
    def wrpuls_file(self, nr):
        with open(file=self.file, mode='a', buffering=-1) as f:
            f.write(nr + "\n")
        return True
        # print("成功")


if __name__ == '__main__':

    # wt_file_name = "C:/Users/xitqa/PythonProjects/edgexDemo/querystr-1.json"
    # wt_file = wrfile(wt_file_name)
    # # if the file already exits, then delete the file firstly
    # wt_file.del_file()
    # # path = pathlib.Path(wt_file_name)
    # # if path.is_file():
    # #     os.remove(wt_file_name)
    #
    # file_name = "C:/Users/xitqa/PythonProjects/edgexDemo/querystr.txt"
    # # create a new file with the same name
    # info_file1 = infoFile(file_name)
    # # check file status
    # print(info_file1.get_file_status())#写入调用方法
    #
    # querystr = wrfile(file_name)
    # # read an exist file
    # querystr_content = querystr.rd_file()
    # print(querystr_content)
    #
    # # write a new file
    # wrpuls_file_rlt = wt_file.wrpuls_file(querystr_content)
    # print(wrpuls_file_rlt)


    rd_file_name = "C:/Users/xitqa/PythonProjects/edgexDemo/mqttMsg-1.json"
    mqttMsg = wrfile(rd_file_name)
    first_line, last_line = mqttMsg.rdTopBottom_file()
    print('文件' + rd_file_name + '第一行为：' + first_line)
    print('文件' + rd_file_name + '最后一行为：' + last_line)

    # 将 JSON 对象转换为 Python 字典
    first_line_dict = json.loads(first_line)
    print(type(first_line_dict))
    print(type(first_line_dict["readings"]))

