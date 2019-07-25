# -*- coding: utf-8 -*-
import collections
import pymysql

from com.caeit.jn2xx.config.configParam import ConfigParameters
from com.caeit.jn2xx.kafkaDbService.mysql.dao.mysqlOperator import MysqlOperator
from com.caeit.jn2xx.kafkaDbService.service.constantValue import *
from com.caeit.jn2xx.kafkaDbService.service.tableRelationship import TableRelationship

"""
0. 为 mysql 数据库提供CRUD服务
"""

__author__ = "Eugene Gao"
__date__ = "2018.08.27"


class MysqlService(object):

    def selectOne(self, dbConnect, table_name, where_orderdict, select_list):
        record_orderdict = MysqlOperator().selectOne(dbConnect, table_name, select_list, where_orderdict)
        # TODO: 返回第一条记录
        return record_orderdict

    def insertSelect(self, dbConnect, table_name, insert_orderdict, select_list):
        # TODO：数据融合功能
        # 1. insert 数据
        MysqlOperator().insert(dbConnect, table_name, insert_orderdict)
        # 2. select 刚 insert 的数据
        record_orderdict = MysqlOperator().selectOne(dbConnect, table_name, select_list, dict({"dxbm": insert_orderdict["dxbm"]}))
        return record_orderdict

    def updateSelect(self, dbConnect, table_name, update_orderdict, where_orderdict, select_list):
        # 1. update 数据
        MysqlOperator().update(dbConnect, table_name, update_orderdict, where_orderdict)
        # 2. selectOne 刚 update 的数据
        record_orderdict = MysqlOperator().selectOne(dbConnect, table_name, select_list, where_orderdict)
        return record_orderdict

    def deleteSelect(self, dbConnect, table_name, where_orderdict, select_list=["dxbm"]):
        # 1.先 selectOne 得到被删除的记录的 dxbm 信息
        record_orderdict = MysqlOperator().selectOne(dbConnect, table_name, select_list, where_orderdict)
        MysqlOperator().delete(dbConnect, table_name, where_orderdict)
        return record_orderdict


def main(dbConnect):
    table_name = "nz_ll_jbsx"

    # 插入表数据---------------------------------------------------------------------------------
    insert_orderdict = collections.OrderedDict()
    insert_orderdict["dxbm"] = "llqg002"
    insert_orderdict["slsj"] = 888888888888003
    insert_orderdict["dxbm1"] = "sbqg001"
    insert_orderdict["dxlb1"] = 1
    insert_orderdict["dxbm2"] = "sbqg002"
    insert_orderdict["dxlb2"] = 2
    insert_orderdict["fx"] = 3
    MysqlService().insertSelect(dbConnect, table_name, insert_orderdict, TableRelationship().table_column_dict[table_name])


    where_orderdict = collections.OrderedDict()
    # where_orderdict["dxbm"] = "llqg010"
    where_orderdict["dxbm1"] = "sbqg001"
    where_orderdict["dxbm2"] = "sbqg002"
    MysqlService().selectOne(dbConnect, table_name, where_orderdict, TableRelationship().table_column_dict[table_name])
    # MysqlService().deleteSelect(dbConnect, table_name, where_orderdict)


if __name__ == "__main__":
    # 配置数据库
    dbconfig_dict = ConfigParameters().dbconfig_local_nz_wltsfx
    # 创建数据库连接
    dbConnect = pymysql.connect(host=dbconfig_dict["host"], port=dbconfig_dict["port"],
                                user=dbconfig_dict["user"], password=dbconfig_dict["password"],
                                database=dbconfig_dict["dataBase"], charset=dbconfig_dict["charset"])
    print(dbconfig_dict)
    main(dbConnect)
    dbConnect.close()