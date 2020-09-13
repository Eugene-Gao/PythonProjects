#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'Eugene Gao'
__date__ = '20200913'

# '''
# pip install apscheduler
# '''

import datetime
import time

from apscheduler.schedulers.blocking import BlockingScheduler

def func():
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func time :', ts)


def func2():
    # 耗时2S
    now = datetime.datetime.now()
    ts = now.strftime('%Y-%m-%d %H:%M:%S')
    print('do func2 time：', ts)
    time.sleep(2)


def dojob():
    # 创建调度器：BlockingScheduler
    scheduler = BlockingScheduler()
    # 添加任务,时间间隔2S
    scheduler.add_job(func, 'interval', seconds=2, id='test_job1')
    # 添加任务,时间间隔5S
    scheduler.add_job(func2, 'interval', seconds=3, id='test_job2')
    scheduler.start()


if __name__ == '__main__':
    dojob()
