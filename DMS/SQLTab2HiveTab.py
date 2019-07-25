#!coding=utf8
#!/usr/bin/python
import pymysql
from impala import dbapi
column_types=["tinyint","smallint","mediumint","int","bigint","float"\
              "double","date","time","year","datetime","timestamp",\
              "char","varchar","tinytext","mediumtext","longtext"]
conn_mysql=pymysql.connect(host='192.168.43.30',user='root',passwd='root',port=3306,db='xiaoka_hive')
conn_dqe=dbapi.connect(host='192.168.43.70',port=21050,database='dms_hive')
cursor_mysql=conn_mysql.cursor()
cursor_dqe=conn_dqe.cursor()
cursor_mysql.execute('show tables')
table_names=[]
for i in cursor_mysql.fetchall():
    table_names.append(i[0])
for table_name in table_names:
    create_table="create table %s("%(table_name)
    primary_key=[]
    cursor_mysql.execute('desc %s'%(table_name))
    table_desces=cursor_mysql.fetchall()
    table_desc_num=len(table_desces)
    for table_desc in table_desces:
        column_name=table_desc[0]
        if 'varchar' in table_desc[1]:
            column_type='string'
        elif 'char' in table_desc[1]:
            column_type='string'
        elif 'bigint' in table_desc[1]:
            column_type = 'bigint'
        elif 'int' in table_desc[1]:
            column_type='int'
        elif 'float' in table_desc[1]:
            column_type='float'
        elif 'double' in table_desc[1]:
            column_type='double'
        if table_desc_num!=1:
            create_table="%s %s %s, "%(create_table,column_name,column_type)
        else:
            create_table="%s %s %s"%(create_table,column_name,column_type)
        table_desc_num-=1

    create_table="%s) stored as parquet"%(create_table)
    print create_table
    cursor_dqe.execute(create_table)