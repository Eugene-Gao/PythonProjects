# -*- coding: utf-8 -*-


__author__ = 'Eugene Gao'
__date__ = '2018.08.10'

import collections
import logging
import json
from datetime import datetime
from log.logUtil import log


def resolve_json(file_name):
    """
    :param file_name: absolute utils path
    :return: json content
    :rtype: collections.OrderedDict()
    """
    json_orderdict = collections.OrderedDict()

    with open(file_name, 'rb') as file:
        for key, value in json.load(file).items():
            json_orderdict[key] = value
            print("key: ", key, "value: ", value, "type of value: ", type(value))
    return json_orderdict


if __name__ == '__main__':
    logger_name = "Delete_llJbsx"
    logger_level = logging.DEBUG
    log_filepath = "C:/Users/xitqa/PythonProjects/edgexDemo/" + logger_name + "_log_" + datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    logger = log(logger_name, logger_level, log_filepath)

    file_name = "C:/Users/xitqa/PythonProjects/TestFiles/SourceDir/Delete_llJbsx.json"
    json_orderdict = resolve_json(file_name)
    print(json_orderdict)
    logger.debug(json_orderdict)