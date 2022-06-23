#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/3/23 15:02
# @Author: JiangXingGang
# @File  : python-snap7.py
import time

import snap7
import struct
import re
from snap7.util import *
from snap7.types import *

client = snap7.client.Client()
client.connect('10.3.19.130', rack=0, slot=1)
if client.get_connected():
    print('连接分拣PLC成功')
else:
    print('连接分拣PLC失败')

while True:
    # 原始数组
    buffer1 = client.read_area(snap7.types.Areas.DB, 8, 274, 4)
    readbuffer1 = snap7.util.get_int(buffer1, 0)
    print(readbuffer1)
    time.sleep(0.5)
# 字符串
#     readstr1 = buffer1.decode('utf-8')
# readstr1 = re.sub(u"([^\u0041-\u005a\u0061-\u007a\u0030-\u0039\u002d])", "", readstr1)

#     buffer2 = client.read_area(snap7.types.Areas.DB, 8, 140, 4)
# # 浮点数
#     readfloat1 = snap7.util.get_real(buffer2, 0)
#     print("原始数组是：",buffer1)
#     print("字符串是：",readstr1)
#
# print("重量是："+"%.3f" % readfloat1+" KG")
