#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/3/31 9:13
# @Author: JiangXingGang
# @File  : python-dingyue.py

from opcua import Client
from opcua import ua
import time


class SubHandler(object):
    def datachange_notification(self, node, val, data):
        print('Python:New data change event',node,val,data)


client = Client("opc.tcp://10.4.20.89:49320")
client.connect()
objects = client.get_objects_node()
root = client.get_root_node()

myvar = client.get_node('ns=2;s=SWBZ_2_PLC_1.SWBZ_2_PLC_1.底部产量')
valuetemp = myvar.get_value()
print(valuetemp)
handler = SubHandler()
sub = client.create_subscription(500,handler)
sub.subscribe_data_change(myvar)
time.sleep(100000)
client.disconnect()
