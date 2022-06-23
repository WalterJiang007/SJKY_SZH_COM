#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/1/17 12:12
# @Author: JiangXingGang
# @File  : tcp_client.py
# -*- coding: utf-8 -*-
import socket  # 导入 socket 模块
import threading
import time

s = socket.socket()  # 创建 socket 对象
host = '10.3.10.142'  # 获取本地主机名
port = 51236  # 设置端口号

s.connect((host, port))

global t


def xunhuandayin():
    str1 = s.recv(50)[1:39]
    print(str1, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    with open('d:\二维码数据', 'a') as f:
        f.write('\n')
        f.write('%s          %s' % (s.recv(50)[1:39], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        f.close()

    t = threading.Timer(0.1, xunhuandayin)
    t.start()


t = threading.Timer(0.1, xunhuandayin)
t.start()
