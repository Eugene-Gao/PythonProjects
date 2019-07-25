# -*- coding: utf-8 -*-
from collections import OrderedDict
"""
表之间的关系可以进一步优化
"""

class TableRelationship(object):
    # 字段信息
    # sb
    nz_sb_jbsx = ["dxbm", "sbmc", "sblx", "jbxx", "kszt", "scck"]
    nz_sb_kzsx_iosb = ["dxbm", "qjbm", "glwlllbh", "mc", "bb"]
    # ll
    nz_ll_jbsx = ["dxbm", "dxbm1", "dxlb1", "dxbm2", "dxlb2", "fx", "slsj"]
    nz_ll_kzsx_idirect = ["dxbm", "tlqssj", "wtmc", "txsblx", "wxmc"]
    # wlpt
    nz_wlpt_jbsx = ["dxbm", "ptlb", "ptlx", "dxfl", "slsj"]
    nz_wlpt_kzsx_fj = ["dxbm", "ph", "jxh", "tdsx", "zbxh"]

    # 表结构信息
    table_column_dict = OrderedDict()
    # sb
    table_column_dict["nz_sb_jbsx"] = nz_sb_jbsx
    table_column_dict["nz_sb_kzsx_iosb"] = nz_sb_kzsx_iosb
    #ll
    table_column_dict["nz_ll_jbsx"] = nz_ll_jbsx
    table_column_dict["nz_ll_kzsx_idirect"] = nz_ll_kzsx_idirect
    #wlpt
    table_column_dict["nz_wlpt_jbsx"] = nz_wlpt_jbsx
    table_column_dict["nz_wlpt_kzsx_fj"] = nz_wlpt_kzsx_fj

    # 表关系信息
    table_relation_dict = OrderedDict()
    # sb
    table_relation_dict["nz_sb_jbsx"] = ["nz_sb_kzsx_iosb"]
    table_relation_dict["nz_sb_kzsx_iosb"] = ["nz_sb_jbsx"]
    # ll
    table_relation_dict["nz_ll_jbsx"] = ["nz_ll_kzsx_idirect"]
    table_relation_dict["nz_ll_kzsx_idirect"] = ["nz_ll_jbsx"]
    # wlpt
    table_relation_dict["nz_wlpt_jbsx"] = ["nz_wlpt_kzsx_fj"]
    table_relation_dict["nz_wlpt_kzsx_fj"] = ["nz_wlpt_jbsx"]
