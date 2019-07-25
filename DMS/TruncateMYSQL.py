#!coding=utf8
#!/usr/bin/python
import pymysql
# from impala import dbapi
conn_dqe=pymysql.connect(host='39.98.187.122',port=4000,user='root',passwd='',db='dms_kudu')
cursor_dqe=conn_dqe.cursor()
cursor_dqe.execute('show tables')
table_names=[]
for i in cursor_dqe.fetchall():
    table_names.append(i[0])
for table_name in table_names:
    cursor_dqe.execute("truncate %s"%table_name)