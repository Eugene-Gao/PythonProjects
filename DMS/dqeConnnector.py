#!coding=utf8
#!/usr/bin/python
import pymysql
from impala import dbapi
conn_dqe=dbapi.connect(host='192.168.200.133',port=21050,database='dms_hive')
cursor_dqe=conn_dqe.cursor()

cursor_dqe.execute("select count(*) from student;")

print cursor_dqe.fetchall()

cursor_dqe.close()
