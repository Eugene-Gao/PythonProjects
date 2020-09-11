# -*- coding: utf-8 -*-

import logging
from datetime import datetime


def log(logger_name, logger_level, log_filepath):
    """output log message to log utils and console

    :param logger_name:
    :param logger_level:
    :param log_filepath:
    :return: logger
    """
    # 创建logger，如果参数为空则返回root logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(logger_level)  # 设置logger日志等级

    # 这里进行判断，如果logger.handlers列表为空，则添加，否则，直接去写日志
    if not logger.handlers:
        # 创建handler
        fh = logging.FileHandler(log_filepath, encoding="utf-8")
        ch = logging.StreamHandler()
    # 设置输出日志格式
    formatter = logging.Formatter(
        fmt="%(asctime)s %(name)s %(filename)s %(message)s",
        datefmt="%Y/%m/%d %X"
    )
    # 为handler指定输出格式
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # 为logger添加的日志处理器
    logger.addHandler(fh)
    logger.addHandler(ch)
    #​直接返回logger
    return logger

if __name__ == '__main__':
    logger_name = "edgeX"
    logger_level = logging.DEBUG
    log_filepath = "C:/Users/xitqa/PythonProjects/edgexDemo/" + logger_name + "_log_" + datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    logConfig_dict = {
        "logger_name": logger_name,
        "logger_level": logger_level,
        "log_filepath": log_filepath
    }
    logger = log(**logConfig_dict)
    logger.warning("警告")
    logger.info("提示")
    logger.error("错误")
    logger.debug("调试")
    logger.debug({"a":2})