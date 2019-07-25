#!coding=utf8
#!/usr/bin/python
import pymysql
from impala import dbapi
conn_dqe=dbapi.connect(host='192.168.43.70',port=21050,database='dms_kudu')
cursor_dqe=conn_dqe.cursor()
cursor_dqe.execute('show tables')
tables=cursor_dqe.fetchall()
for table in tables:
    table_name=table[0]
    cursor_dqe.execute("describe %s"%(table_name))
    column_name=[]
    for column_result in cursor_dqe.fetchall():
        column_name.append(column_result[0])
        print column_name
    if 'pictureftp' not in column_name:
       # continue
    #else:
     #   cursor.execute('alter table %s add column SLSJ bigint'%(table_name))
      #  cursor.execute('alter table %s add column GXSJ bigint'%(table_name))
       # cursor.execute('alter table %s add column SCBZ int'%(table_name))
        cursor_dqe.execute('alter table %s add columns(pictureftp string)'%(table_name))
