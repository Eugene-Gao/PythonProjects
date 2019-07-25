#!coding=utf8
#!/usr/bin/python
import pymysql
from impala import dbapi
conn_dqe=dbapi.connect(host='192.168.200.133',port=10080,database='dms_hive')
cursor_dqe=conn_dqe.cursor()
cursor_dqe.execute('show tables')
table_names=[]
for i in cursor_dqe.fetchall():
    table_names.append(i[0])
for table_name in table_names:
    cursor_dqe.execute("show create table %s"%table_name)
    create_sql=cursor_dqe.fetchall()
    print create_sql