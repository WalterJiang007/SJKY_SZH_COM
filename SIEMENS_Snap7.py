#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/3/23 15:02
# @Author: JiangXingGang
# @File  : python-snap7.py
import threading

import snap7
import struct
import re
from snap7.util import *
from snap7.types import *

client = snap7.client.Client()
client.connect('10.3.19.120', rack=0, slot=1)
if client.get_connected():
    print('连接码垛PLC成功')
else:
    print('连接码垛PLC失败')

global t


def xunhuandayin():
    buffer1 = client.read_area(snap7.types.Areas.DB, 146, 134, 1)

    print(buffer1, time.strftime("%Y-%m-%d %H:%M:%S:%MS", time.localtime()))
    t = threading.Timer(0.2, xunhuandayin)
    t.start()


t = threading.Timer(0.2, xunhuandayin)
t.start()

# readstr1 = buffer1.decode('utf-8')
# readstr1 = re.sub(u"([^\u0041-\u005a\u0061-\u007a\u0030-\u0039\u002d])", "", readstr1)
#
# buffer2 = client.read_area(snap7.types.Areas.DB, 130, 130, 128)
# print(buffer2)
# # readstr2 = buffer2.decode('utf-8')
# # readstr2 = re.sub(u"([^\u0041-\u005a\u0061-\u007a\u0030-\u0039\u002d])", "", readstr2)
#
# buffer3 = client.read_area(snap7.types.Areas.DB, 130, 260, 128)
# print(buffer3)
# # readstr3 = buffer3.decode('utf-8')
# # readstr3 = re.sub(u"([^\u0041-\u005a\u0061-\u007a\u0030-\u0039\u002d])", "", readstr3)
#
# buffer4 = client.read_area(snap7.types.Areas.DB, 130, 390, 128)
# print(buffer4)
# # readstr4 = buffer4.decode('utf-8')
# # readstr4 = re.sub(u"([^\u0041-\u005a\u0061-\u007a\u0030-\u0039\u002d])", "", readstr4)
#
# print('1#扫码枪信息:''\r\n', readstr1)
# print('2#扫码枪信息:''\r\n', readstr2)
# print('3#扫码枪信息:''\r\n', readstr3)
# print('4#扫码枪信息:''\r\n', readstr4)
#
# # client.write_area(snap7.types.Areas.DB, 130, 407, b'#\x00\x10')
# #
# # buffer5 = client.read_area(snap7.types.Areas.DB, 130, 408, 2)
# # print(buffer5)
