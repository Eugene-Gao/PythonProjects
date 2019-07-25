# -*- coding: utf-8 -*-
import collections
import functools

import pymysql
from com.caeit.jn2xx.config.configParam import ConfigParameters
from com.caeit.jn2xx.utils.datatypeUtil import strWrappedQuota

"""
0. 提供数据库增、删、改、查基本功能
1. 安装pymysql模块  pip3 install pymysql

"""
__author__ = "Eugene Gao"
__date__ = "2018.08.10"


class MysqlOperator(object):
    # 数据库增、删、改、查等操作的装饰器，用来控制数据库连接行为
    def dbOpenClose(func):
        @functools.wraps(func)
        def run(self, db, *args, **kwargs):
            print("call %s():" % func.__name__)
            # 创建游标
            cursor = db.cursor()
            try:
                # 运行sql语句
                cursor.execute(func(self, db, *args, **kwargs))
                # 得到返回值
                results = cursor.fetchall()
                print("execute results: ", type(results), len(results), results)
                # 提交事务
                db.commit()
            except Exception as e:
                # 如果出现错误，回滚事务
                db.rollback()
                # 打印报错信息
                print("运行", str(func), "方法时出现错误，错误代码：", e)
            finally:
                # 关闭游标和数据库连接
                cursor.close()
            try:
                # 返回sql执行信息
                return results
            except Exception as e:
                print("没有得到返回值，请检查代码，该信息出现在 MysqlOperator 类中的装饰器方法")
            finally:
                pass

        return run

    @dbOpenClose
    def exec_staticsql(self, dbConnect, sql):
        print("exec_staticsql sql：", sql)
        return sql
    
    @dbOpenClose
    def create_table(self, dbConnect, table_name, fields_orderdict):
        # 使用预处理语句创建表
        sql = "create table if not exists " + table_name + " ( "
        for key, value in fields_orderdict.items():
            sql = sql + key + " " + value + ", "
        # 删除最后的逗号, 增加右侧括号
        sql = sql[:-2] + " )"

        print("create_table sql：", sql)
        return sql

    @dbOpenClose
    def insert(self, dbConnect, table_name, fields_orderdict):
        fieldsql = ''
        valuesql = ''
        for key, value in fields_orderdict.items():
            fieldsql += key + ", "
            valuesql += strWrappedQuota(value) + ", "

        # 删除最后的 ", "
        fieldsql = fieldsql[:-2]
        valuesql = valuesql[:-2]
        sql = "insert into " + table_name + " ( " + fieldsql + " ) values ( " + valuesql + " )"
        print("insert sql：", sql)
        return sql

    @dbOpenClose
    def __select(self, dbConnect, table_name, select_list, where_orderdict):
        selectsql = ''
        for key in select_list:
            selectsql += key + ", "
        # 删除最后的 ", "
        selectsql = selectsql[:-2]

        wheresql = ''
        for key,value in where_orderdict.items():
            wheresql += key + " =  " + strWrappedQuota(value) + " and "
        # 删除最后的 "and "
        wheresql = wheresql[:-4]
        sql = "select " + selectsql + " from " + table_name + " where " + wheresql
        print("select sql：", sql)
        return sql

    @dbOpenClose
    def update(self, dbConnect, table_name, update_orderdict, where_orderdict):
        updatesql = ''
        for key, value in update_orderdict.items():
            updatesql += key + " =  " + strWrappedQuota(value) + ", "
        # 删除最后的 "and "
        updatesql = updatesql[:-2]

        wheresql = ''
        for key, value in where_orderdict.items():
            wheresql += key + " =  " + strWrappedQuota(value) + " and "
        # 删除最后的 "and "
        wheresql = wheresql[:-4]
        sql = "update " + table_name + " set " + updatesql + " where " + wheresql
        print("update sql：", sql)
        return sql

    @dbOpenClose
    def delete(self, dbConnect, table_name, where_orderdict):
        wheresql = ''
        for key, value in where_orderdict.items():
            wheresql += key + " =  " + strWrappedQuota(value) + " and "
        # 删除最后的 "and "
        wheresql = wheresql[:-4]
        sql = "delete from " + table_name + " where " + wheresql
        print("delete sql：", sql)
        return sql


    def selectAll(self, dbConnect, table_name, select_list, where_orderdict):
        """
        支持返回多条记录
        :param dbConnect: 数据库连接
        :param table_name: 操作表名
        :param select_list: SQL selectOne 字段构成的 list
        :param where_orderdict: SQL where 字段构成的 dict
        :return: fetchRecord_list：长度为0表示没有结果，支持返回多条 record 的list，每个 list中的元素就是一行 record
        """
        fetchRecord_list = list()
        record_list = self.__select(dbConnect, table_name, select_list, where_orderdict)
        if len(record_list) == 0:
            return fetchRecord_list
        else:
            for recordIdx in range(0, len(record_list)):
                record = record_list[recordIdx]
                fetch_orderdict = collections.OrderedDict()
                for index in range(0, len(record)):
                    fetch_orderdict[select_list[index]] = record[index]

                print("MysqlOperator:selectOne:fetch_orderdict: ", fetch_orderdict)
                fetchRecord_list.append(fetch_orderdict)

            return fetchRecord_list

    def selectOne(self, dbConnect, table_name, select_list, where_orderdict):
        # 返回一条记录
        fetchRecord_list = self.selectAll(dbConnect, table_name, select_list, where_orderdict)
        if len(fetchRecord_list) == 0:
            return fetchRecord_list
        else:
            # 如果记录不为空，则返回第一条记录
            return fetchRecord_list[0]



def main(dbConnect):
    table_name = "employee"
    # 删除表---------------------------------------------------------------------------------
    staticsql = "drop table if exists " + table_name
    MysqlOperator().exec_staticsql(dbConnect, staticsql)

    # 创建表---------------------------------------------------------------------------------
    fields_orderdict = collections.OrderedDict()
    fields_orderdict["first_name"] = "char(20) not null"
    fields_orderdict["last_name"] = "char(20)"
    fields_orderdict["bir"] = "datetime"
    fields_orderdict["age"] = "int"
    fields_orderdict["sex"] = "char(1)"
    fields_orderdict["income"] = "double"
    MysqlOperator().create_table(dbConnect, table_name, fields_orderdict)

    #插入表数据---------------------------------------------------------------------------------
    # insertsql = '''insert into employee (first_name, last_name, bir, age, sex, income)
    #                         values ("shumeng", "zhu", "1982-07-31 19:30:00", 32, "f", 7500)'''
    fields_orderdict["first_name"] = "minhe"
    fields_orderdict["last_name"] = "gao"
    fields_orderdict["bir"] = "2015-02-01 19:30:00"
    fields_orderdict["age"] = 3
    fields_orderdict["sex"] = "M"
    fields_orderdict["income"] = 40000.75
    MysqlOperator().insert(dbConnect, table_name, fields_orderdict)

    # 查询表数据---------------------------------------------------------------------------------
    # selectsql = '''selectOne * from employee where first_name = 'qian' and last_name = 'gao' '''
    select_list = list(fields_orderdict.keys())
    where_orderdict = collections.OrderedDict()
    # where_orderdict = {column_name : value}
    where_orderdict["first_name"] = "minhe"
    where_orderdict["last_name"] = "gao"
    fetchRecord_list = MysqlOperator().selectOne(dbConnect, table_name, select_list, where_orderdict)


    # 更新表数据---------------------------------------------------------------------------------
    # updatesql = '''update employee set income = 50000.55 where first_name = 'minhe' and last_name = 'gao' '''
    update_orderdict = collections.OrderedDict()
    # update_orderdict = {column_name : value}
    update_orderdict["income"] = 6000.66
    where_orderdict = collections.OrderedDict()
    # where_orderdict = {column_name : value}
    where_orderdict["first_name"] = "minhe"
    where_orderdict["last_name"] = "gao"
    MysqlOperator().update(dbConnect, table_name, update_orderdict, where_orderdict)

    # 删除表数据---------------------------------------------------------------------------------
    # deletesql = '''delete from employee where first_name = 'minhe' and last_name = 'gao' '''
    MysqlOperator().delete(dbConnect, table_name, where_orderdict)

if __name__ == "__main__":
    # 配置数据库
    dbconfig_dict = ConfigParameters().dbconfig_local_test
    # 创建数据库连接
    dbConnect = pymysql.connect(host=dbconfig_dict["host"], port=dbconfig_dict["port"],
                                user=dbconfig_dict["user"], password=dbconfig_dict["password"],
                                database=dbconfig_dict["dataBase"], charset=dbconfig_dict["charset"])
    print(dbconfig_dict)
    main(dbConnect)
    dbConnect.close()
