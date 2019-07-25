#!coding=utf8
#!/usr/bin/python
import pymysql
from hdfs.client import Client
from impala import dbapi
import os

####################
database="xiaoka_kudu"##############需要设置参数
external_database="external_%s"%(database)
kudu_database="xiaoka_kudu"###################需要设置参数
os.system("$dqe -q 'create database if not exists %s'"%external_database)
####################
hdfs_client=Client("http://bigdata4:50070")
hdfs_client.makedirs('/tmp/external_tables/%s'%(external_database));
column_types=["tinyint","smallint","mediumint","int","bigint","float"\
              "double","date","time","year","datetime","timestamp",\
              "char","varchar","tinytext","mediumtext","longtext"]
conn_mysql=pymysql.connect(host='bigdata4',user='root',passwd='root',port=3306,db='%s'%database)
conn_dqe=dbapi.connect(host='bigdata4',port=21050,database='%s'%external_database)
cursor_mysql=conn_mysql.cursor()
cursor_dqe=conn_dqe.cursor()
cursor_mysql.execute('show tables')
table_names=[]
for i in cursor_mysql.fetchall():
    table_names.append(i[0])

for table_name in table_names:
    os.system("mkdir -p /home/tmp/mysql_outfile/%s"%database)
    os.system("chown -R mysql:mysql /home/tmp/mysql_outfile/%s"%database)
#    os.system("rm -rf /home/tmp/mysql_outfile/%s"%(table_name))
    cursor_mysql.execute('''select * from %s into outfile '/home/tmp/mysql_outfile/%s/%s' fields terminated by '`' lines terminated by '^' '''%(table_name,database,table_name))
#    hdfs_client.delete('/tmp/external_tables/%s/%s'%(database_name,table_name))
    hdfs_client.makedirs('/tmp/external_tables/%s/%s/'%(external_database,table_name));
    hdfs_client.upload('/tmp/external_tables/%s/%s/'%(external_database,table_name), '/home/tmp/mysql_outfile/%s/%s'%(database,table_name))
    create_external_table="create external table %s("%(table_name)
    cursor_mysql.execute('desc %s'%(table_name))
    table_desces=cursor_mysql.fetchall()
    table_desc_num=len(table_desces)
    for table_desc in table_desces:
        column_name=table_desc[0]
        if 'char' in table_desc[1]:
            column_type='string'
        elif 'varchar' in table_desc[1]:
            column_type='string'
        elif 'int' in table_desc[1]:
            column_type='int'
        elif 'bigint' in table_desc[1]:
            column_type='bigint'
        elif 'float' in table_desc[1]:
            column_type='float'
        elif 'double' in table_desc[1]:
            column_type='double'
        elif 'decimal' in table_desc[1]:
            column_type='double'
        if table_desc_num!=1:
            create_external_table="%s %s %s, "%(create_external_table,column_name,column_type)
        else:
            create_external_table="%s %s %s"%(create_external_table,column_name,column_type)
        table_desc_num-=1
    create_external_table="%s) row format delimited fields terminated by '`' lines terminated by '^' location '/tmp/external_tables/%s/%s/'"%(create_external_table,external_database,table_name)
    print create_external_table
    cursor_dqe.execute("drop table if exists %s.%s"%(external_database,table_name))
    cursor_dqe.execute(create_external_table)
    cursor_dqe.execute("insert into %s.%s select * from %s.%s"%(kudu_database,table_name,external_database,table_name))
