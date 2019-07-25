import pymysql
conn=pymysql.connect(host='192.168.43.30',port=3306,user='root',passwd='root',db='xiaoka_kudu')
cursor=conn.cursor()
cursor.execute('show tables')
tables=cursor.fetchall()
for table in tables:
    table_name=table[0]
    cursor.execute("desc %s"%(table_name))
    column_name=[]
    for column_result in cursor.fetchall():
        column_name.append(column_result[0])
        print column_name
    if 'SLSJALLCOLUMNS' in column_name:
       # continue
    #else:
     #   cursor.execute('alter table %s add column SLSJ bigint'%(table_name))
      #  cursor.execute('alter table %s add column GXSJ bigint'%(table_name))
       # cursor.execute('alter table %s add column SCBZ int'%(table_name))
        cursor.execute('alter table %s drop column SLSJALLCOLUMNS'%(table_name))
