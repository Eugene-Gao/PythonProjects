# -*- coding: utf-8 -*-

"""
0. 利用 kafka 消息总线，
1. 解析Json文件，得到 dict 对象
2. 根据“sql_operator”，执行增、删、改操作
"""
import pymysql
import collections

from com.caeit.jn2xx.config.configParam import ConfigParameters
from com.caeit.jn2xx.utils.fileUtil import resolve_json
from com.caeit.jn2xx.kafkaDbService.service.constantValue import *
from com.caeit.jn2xx.kafkaDbService.service.mysqlService import MysqlService
from com.caeit.jn2xx.kafkaDbService.service.tableRelationship import TableRelationship

__author__ = "Eugene Gao"
__date__ = "2018.08.27"


def setDxlb(tableName):
    print("对象类别，设备：1，链路：2，平台：3 ,子网：4-----------------------------------------------------")
    if tableName.lower().startswith("nz_sb_"):
        dxlb = SHE_BEI
    elif tableName.lower().startswith("nz_ll_"):
        dxlb = LIAN_LU
    elif tableName.lower().startswith("nz_wlpt_"):
        dxlb = PING_TAI
    elif tableName.lower().startswith("nz_zw_"):
        dxlb = ZI_WANG
    else:
        print("The current table name is: ", tableName.lower())
    return dxlb


def doBaseTableMsg(dbConnect, sqlOperator, tableName, msg_dict):
    """
    进行操作表数据库表操作
    :param dbConnect: 数据库连接
    :param sqlOperator: 增、删、改
    :param tableName: 操作表名
    :param msg_dict: sql 语句相关信息
    :return: 操作执行的记录
    """
    print("switch 删：0；增：1；改：2 -----------------------------------------------------")
    if sqlOperator == DELETE_OPERATION:
        record = MysqlService().deleteSelect(dbConnect, \
                                             tableName, msg_dict["where_fields"],
                                             TableRelationship().table_column_dict[tableName])
    elif sqlOperator == INSERT_OPERATION:
        record = MysqlService().insertSelect(dbConnect, \
                                             tableName, msg_dict["insert_fields"],
                                             TableRelationship().table_column_dict[tableName])
    elif sqlOperator == UPDATE_OPERATION:
        record = MysqlService().updateSelect(dbConnect, \
                                             tableName, msg_dict["set_fields"], msg_dict["where_fields"],
                                             TableRelationship().table_column_dict[tableName])
    else:
        print("sql_operator has an invalid value: ", sqlOperator)
        record = dict()

    return record


def getRelatedTableMsg(dbConnect, tableName_list, where_dict):
    """
    进行关联表数据库表操作
    :param dbConnect: 数据库连接
    :param tableName_list: 关联表名 List
    :param where_dict: select 关联记录的 where 信息
    :return: [关联表名，关联记录]
    """
    relatedTable = ""
    record = collections.OrderedDict()
    # 迭代相关表的 list
    for tableName in tableName_list:
        record_orderdict = MysqlService().selectOne(dbConnect, tableName, where_dict,
                                                    TableRelationship().table_column_dict[tableName])
        # 如果 selectOne 有效记录，则结束迭代
        if len(record_orderdict) > 0:
            relatedTable = tableName
            record = record_orderdict
            break

    return [relatedTable, record]


def databaseService(dbConnect, msg_dict):
    """
    根据“sql_operator”，执行增、删、改操作
    :param dbConnect: 数据库连接
    :param msg_dict: Json 文件解析之后得到的 dict 对象
    :return: 推送给其他系统的 view_orderdict
    """
    sqlOperator = msg_dict["sql_operator"]
    tableName = msg_dict["table_name"]
    # 是基本表，还是扩展表
    if tableName.lower().find("kz") > -1:  # 操作表是扩展表
        # 得到扩展表信息
        kzxx = doBaseTableMsg(dbConnect, sqlOperator, tableName, msg_dict)
        # 得到基本表信息
        [relatedTableName, jbxx] = getRelatedTableMsg(dbConnect, TableRelationship().table_relation_dict[tableName],
                                                      dict({"dxbm": kzxx["dxbm"]}))
        view_orderdict = collections.OrderedDict()
        view_orderdict["bjzd"] = sqlOperator
        view_orderdict["dxlb"] = setDxlb(tableName)
        view_orderdict["dxbm"] = kzxx["dxbm"]
        view_orderdict["jbxx"] = jbxx
        view_orderdict["kzxx"] = kzxx
        view_orderdict["jb_table"] = relatedTableName
        view_orderdict["kz_table"] = tableName
    else:  # 基本表
        jbxx = doBaseTableMsg(dbConnect, sqlOperator, tableName, msg_dict)
        # 得到基本表信息
        [relatedTableName, kzxx] = getRelatedTableMsg(dbConnect, TableRelationship().table_relation_dict[tableName],
                                                      dict({"dxbm": jbxx["dxbm"]}))
        view_orderdict = collections.OrderedDict()
        view_orderdict["bjzd"] = sqlOperator
        view_orderdict["dxlb"] = setDxlb(tableName)
        view_orderdict["dxbm"] = jbxx["dxbm"]
        view_orderdict["jbxx"] = jbxx
        view_orderdict["kzxx"] = kzxx
        view_orderdict["jb_table"] = tableName
        view_orderdict["kz_table"] = relatedTableName

    print("databaseService:main:view_orderdict: ", view_orderdict)
    return view_orderdict


def main():
    # 设备
    # fileName = "D:/Work/Project/PythonProjects/TestFiles/SourceDir/Insert_sbJbsx.json"
    # 链路
    # jb_table
    fileName = "D:/Work/Project/PythonProjects/TestFiles/SourceDir/Insert_llJbsx.json"
    # fileName = "D:/Work/Project/PythonProjects/TestFiles/SourceDir/Update_llJbsx.json"
    # fileName = "D:/Work/Project/PythonProjects/TestFiles/SourceDir/Delete_llJbsx.json"
    # kz_table
    # fileName = "D:/Work/Project/PythonProjects/TestFiles/SourceDir/Insert_llKzsxIdirect.json"
    # fileName = "D:/Work/Project/PythonProjects/TestFiles/SourceDir/Update_llKzsxIdirect.json"
    # fileName = "D:/Work/Project/PythonProjects/TestFiles/SourceDir/Delete_llKzsxIdirect.json"

    # 配置数据库
    dbconfig_dict = ConfigParameters().dbconfig_local_nz_wltsfx
    # 创建数据库连接
    dbConnect = pymysql.connect(host=dbconfig_dict["host"], port=dbconfig_dict["port"],
                                user=dbconfig_dict["user"], password=dbconfig_dict["password"],
                                database=dbconfig_dict["dataBase"], charset=dbconfig_dict["charset"])
    print(dbconfig_dict)
    # 模拟通过 kafka 获得消息，转化为 dict 对象
    msg_dict = resolve_json(fileName)
    print("dict from Json utils: ", msg_dict)

    viewMsg = databaseService(dbConnect, msg_dict)
    dbConnect.close()

# if __name__ == "__main__":
#     main()
