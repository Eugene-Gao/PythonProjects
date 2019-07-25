#!coding=utf8
#!/usr/bin/python
import pymysql

conn_mysql=pymysql.connect(host='192.168.43.30',user='root',passwd='root',\
                           port=3306,db='xiaoka_kudu')
cursor_mysql=conn_mysql.cursor()
# cursor_dqe=conn_dqe.cursor()
cursor_mysql.execute('show tables')
table_names=[]
table_without_pk=[]
table_many_pk=[]
table_disorder_pk=[]
for i in cursor_mysql.fetchall():
    table_names.append(i[0])

for table_name in table_names:
    hasPK=1
    # PKposition=0
    # PKamount=0
    cursor_mysql.execute("desc %s"%table_name)
    for column_description in cursor_mysql.fetchall():
        if 'PRI' in column_description:
            hasPK=0
            break
    if hasPK==1:
        table_without_pk.append(table_name)

print table_without_pk

for table_name in table_names:
    # hasPK=1
    PKposition=0
    # PKamount=0
    cursor_mysql.execute("desc %s"%table_name)
    for column_description in cursor_mysql.fetchall():
        if 'PRI' in column_description:
            PKposition+=1
            break
        PKposition+=1
    if PKposition > 1:
        table_disorder_pk.append(table_name)
print table_disorder_pk

for table_name in table_names:
    # hasPK=1
    # PKposition=0
    PKamount=0
    cursor_mysql.execute("desc %s"%table_name)
    for column_description in cursor_mysql.fetchall():
        if 'PRI' in column_description:
            PKamount+=1
    if PKamount > 1:
        table_many_pk.append(table_name)
print table_many_pk
