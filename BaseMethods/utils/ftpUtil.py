# coding: utf-8
import ftplib
import os
from ftplib import FTP
import time


def ftpconnect(host, username, password):
    ftp = FTP()
    # ftp.set_debuglevel(2)         #打开调试级别2，显示详细信息
    ftp.connect(host, 21)  # 连接
    ftp.login(username, password)  # 登录，如果匿名登录则用空串代替即可
    # 切换到files目录
    ftp.cwd('files')
    return ftp


# remotepath即服务器上文件名，localpath即本地新建并且要写入的文件名
def downloadfile(ftp, remotepath, localpath):
    bufsize = 1024  # 设置缓冲块大小
    # ftp.cwd('files')
    fp = open(localpath, 'wb')  # 以写模式在本地打开文件
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)  # 接收服务器上文件并写入本地文件
    ftp.set_debuglevel(0)  # 关闭调试
    fp.close()  # 关闭文件


# remotepath即服务器上新建并且要写入的文件名，localpath即本地要上传的文件名
def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    # ftp.cwd('files')
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)  # 上传文件
    ftp.set_debuglevel(0)
    fp.close()


# 使用os模块walk函数，搜索出某目录下的全部文件
######################获取同一个文件夹下的所有文件名#######################
def getLocalFileName(filepath):
    file_list = []
    for root, dirs, files in os.walk(filepath):
        for filespath in files:
            # print(os.path.join(root, filespath))
            # file_list.append(os.path.join(root, filespath))
            file_list.append(filespath)

    return file_list


# 使用ftp库nlst函数，搜索出ftp目录下的全部文件名和目录名
######################获取同一个文件夹下的所有文件名和目录名#######################
def getRemoteFileName(ftp):
    file_list = []
    try:
        file_list = ftp.nlst()
    except ftplib.error_perm as resp:
        if str(resp) == "550 No files found":
            print("No files in this directory")
        else:
            raise

    return file_list


# ftp1为远程ftp服务器，ftp2为本地ftp服务器，imageStr为远程ftp服务器上要下载的文件名
def imageProcess(ftp1, ftp2, imageStr):
    files = getRemoteFileName(ftp1)
    # print len(files)
    # 如果远程ftp服务器某目录下没有文件或目录，直接退出程序
    if (len(files) == 0):
        exit(1)
    # for f in files:
    #    print f

    time_int = time.time()
    # local_str = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    local_str = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    # print  type(local_str), local_str

    # 指定要从远程ftp服务器上下载的文件，这里举例为readme.jpg
    # 下载到本地的文件名,在原文件名上加了时间前缀
    localpath = local_str + '-' + imageStr
    # print localpath
    # 下载到本地
    downloadfile(ftp1, imageStr, localpath)

    # 设置本地ftp服务器的文件的名字，用来存储下载的文件
    remotepath = os.path.basename(localpath)
    # 上传下载的文件到本地ftp服务器，文件名字不变
    uploadfile(ftp2, remotepath, localpath)
    # 删除本地下载的临时文件
    os.remove(localpath)

    return remotepath


if __name__ == "__main__":
    ftp = ftpconnect("192.168.239.142", "sammy", "123456")

    gFile = "readme.jpg"

    # 为测试方便，这里远程ftp服务器和本地ftp服务器为同一ftp服务器
    fileName = imageProcess(ftp, ftp, gFile)

    print(fileName)

    ftp.quit()
