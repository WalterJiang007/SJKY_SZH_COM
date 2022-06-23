#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/5/20 15:34
# @Author: JiangXingGang
# @File  : 钉钉报警.py

# coding: utf-8
import json
import requests
import opcua.ua
import threading
import time
from opcua import Client


# 发送钉钉消息
def send_dingtalk_message(url, content, mobile_list):
    headers = {'Content-Type': 'application/json'}
    data = {
        "msgtype": "text",
        "text": {
            # 要发送的内容【支持markdown】【！注意：content内容要包含机器人自定义关键字，不然消息不会发送出去，这个案例中是test字段】
            "content": content
        },
        "at": {
            # 要@的人
            "atMobiles": mobile_list,
            # 是否@所有人
            "isAtAll": False
        }
    }
    r = requests.post(url, headers=headers, data=json.dumps(data))
    print(r.text)
    return r.text


client = Client("opc.tcp://10.4.20.89:49320")
# 获取dingtalk token url
access_token = 'https://oapi.dingtalk.com/robot/send?access_token' \
               '=94e59fc247543002575479dde4d8283fa780fe5f2d82ab637ebf326f25eb2534 '


try:
    client.connect()

    sa1 = client.get_node('ns=2;s=SWBZ_2_PLC_1.SWBZ_2_PLC_1._System._SecondsInError')
    sa_1 = sa1.get_value()
    if sa_1 == 0:
        IN_number_1 = client.get_node('ns=2;s=SWBZ_2_PLC_1.SWBZ_2_PLC_1.飞达产量')
        IN_1 = IN_number_1.get_value()
        OUT_number_1 = client.get_node('ns=2;s=SWBZ_2_PLC_1.SWBZ_2_PLC_1.底部产量')
        OUT_1 = OUT_number_1.get_value()
        if IN_1 < OUT_1 - 200:
            content = '产量报警：1号机飞达产量:' + str(IN_1) + ';底部产量:' + str(OUT_1) + ',异常,请检查'
            mobile_list = ['173xxxxxx']
            # 发送钉钉消息
            send_dingtalk_message(access_token, content, mobile_list)

    sa2 = client.get_node('ns=2;s=SWBZ_2_PLC_2.SWBZ_2_PLC_2._System._SecondsInError')
    sa_2 = sa2.get_value()
    if sa_2 == 0:
        IN_number_2 = client.get_node('ns=2;s=SWBZ_2_PLC_2.SWBZ_2_PLC_2.飞达产量')
        IN_2 = IN_number_2.get_value()
        OUT_number_2 = client.get_node('ns=2;s=SWBZ_2_PLC_2.SWBZ_2_PLC_2.底部产量')
        OUT_2 = OUT_number_2.get_value()
        if IN_2 < OUT_2 - 200:
            content = '产量报警：2号机飞达产量:' + str(IN_2) + ';底部产量:' + str(OUT_2) + ',异常,请检查'
            mobile_list = ['173xxxxxx']
            # 发送钉钉消息
            send_dingtalk_message(access_token, content, mobile_list)

    sa3 = client.get_node('ns=2;s=SWBZ_2_PLC_3.SWBZ_2_PLC_3._System._SecondsInError')
    sa_3 = sa3.get_value()
    if sa_3 == 0:
        IN_number_3 = client.get_node('ns=2;s=SWBZ_2_PLC_3.SWBZ_2_PLC_3.飞达产量')
        IN_3 = IN_number_3.get_value()
        OUT_number_3 = client.get_node('ns=2;s=SWBZ_2_PLC_3.SWBZ_2_PLC_3.底部产量')
        OUT_3 = OUT_number_3.get_value()
        if IN_3 < OUT_3 - 200:
            content = '产量报警：3号机飞达产量:' + str(IN_3) + ';底部产量:' + str(OUT_3) + ',异常,请检查'
            mobile_list = ['173xxxxxx']
            # 发送钉钉消息
            send_dingtalk_message(access_token, content, mobile_list)
    sa4 = client.get_node('ns=2;s=SWBZ_2_PLC_4.SWBZ_2_PLC_4._System._SecondsInError')
    sa_4 = sa4.get_value()
    if sa_4 == 0:
        IN_number_4 = client.get_node('ns=2;s=SWBZ_2_PLC_4.SWBZ_2_PLC_4.飞达产量')
        IN_4 = IN_number_4.get_value()
        OUT_number_4 = client.get_node('ns=2;s=SWBZ_2_PLC_4.SWBZ_2_PLC_4.底部产量')
        OUT_4 = OUT_number_4.get_value()
        if IN_4 < OUT_4 - 200:
            content = '产量报警：4号机飞达产量:' + str(IN_4) + ';底部产量:' + str(OUT_4) + ',异常,请检查'
            mobile_list = ['174xxxxxx']
            # 发送钉钉消息
            send_dingtalk_message(access_token, content, mobile_list)

    sa5 = client.get_node('ns=2;s=SWBZ_2_PLC_5.SWBZ_2_PLC_5._System._SecondsInError')
    sa_5 = sa5.get_value()
    if sa_5 == 0:
        IN_number_5 = client.get_node('ns=2;s=SWBZ_2_PLC_5.SWBZ_2_PLC_5.飞达产量')
        IN_5 = IN_number_5.get_value()
        OUT_number_5 = client.get_node('ns=2;s=SWBZ_2_PLC_5.SWBZ_2_PLC_5.底部产量')
        OUT_5 = OUT_number_5.get_value()
        if IN_5 < OUT_5 - 200:
            content = '产量报警：5号机飞达产量:' + str(IN_5) + ';底部产量:' + str(OUT_5) + ',异常,请检查'
            mobile_list = ['175xxxxxx']
            # 发送钉钉消息
            send_dingtalk_message(access_token, content, mobile_list)

    sa6 = client.get_node('ns=2;s=SWBZ_2_PLC_6.SWBZ_2_PLC_6._System._SecondsInError')
    sa_6 = sa6.get_value()
    if sa_6 == 0:
        IN_number_6 = client.get_node('ns=2;s=SWBZ_2_PLC_6.SWBZ_2_PLC_6.飞达产量')
        IN_6 = IN_number_6.get_value()
        OUT_number_6 = client.get_node('ns=2;s=SWBZ_2_PLC_6.SWBZ_2_PLC_6.底部产量')
        OUT_6 = OUT_number_6.get_value()
        if IN_6 < OUT_6 - 200:
            content = '产量报警：6号机飞达产量:' + str(IN_6) + ';底部产量:' + str(OUT_6) + ',异常,请检查'
            mobile_list = ['176xxxxxx']
            # 发送钉钉消息
            send_dingtalk_message(access_token, content, mobile_list)

    sa7 = client.get_node('ns=2;s=SWBZ_2_PLC_7.SWBZ_2_PLC_7._System._SecondsInError')
    sa_7 = sa7.get_value()
    if sa_7 == 0:
        IN_number_7 = client.get_node('ns=2;s=SWBZ_2_PLC_7.SWBZ_2_PLC_7.飞达产量')
        IN_7 = IN_number_7.get_value()
        OUT_number_7 = client.get_node('ns=2;s=SWBZ_2_PLC_7.SWBZ_2_PLC_7.底部产量')
        OUT_7 = OUT_number_7.get_value()
        if IN_7 < OUT_7 - 200:
            content = '产量报警：7号机飞达产量:' + str(IN_7) + ';底部产量:' + str(OUT_7) + ',异常,请检查'
            mobile_list = ['177xxxxxx']
            # 发送钉钉消息
            send_dingtalk_message(access_token, content, mobile_list)

    sa8 = client.get_node('ns=2;s=SWBZ_2_PLC_8.SWBZ_2_PLC_8._System._SecondsInError')
    sa_8 = sa8.get_value()
    if sa_8 == 0:
        IN_number_8 = client.get_node('ns=2;s=SWBZ_2_PLC_8.SWBZ_2_PLC_8.飞达产量')
        IN_8 = IN_number_8.get_value()
        OUT_number_8 = client.get_node('ns=2;s=SWBZ_2_PLC_8.SWBZ_2_PLC_8.底部产量')
        OUT_8 = OUT_number_8.get_value()
        if IN_8 < OUT_8 - 200:
            content = '产量报警：8号机飞达产量:' + str(IN_8) + ';底部产量:' + str(OUT_8) + ',异常,请检查'
            mobile_list = ['178xxxxxx']
            # 发送钉钉消息
            send_dingtalk_message(access_token, content, mobile_list)

    sa9 = client.get_node('ns=2;s=SWBZ_2_PLC_9.SWBZ_2_PLC_9._System._SecondsInError')
    sa_9 = sa9.get_value()
    if sa_9 == 0:
        IN_number_9 = client.get_node('ns=2;s=SWBZ_2_PLC_9.SWBZ_2_PLC_9.飞达产量')
        IN_9 = IN_number_9.get_value()
        OUT_number_9 = client.get_node('ns=2;s=SWBZ_2_PLC_9.SWBZ_2_PLC_9.底部产量')
        OUT_9 = OUT_number_9.get_value()
        if IN_9 < OUT_9 - 200:
            content = '产量报警：9号机飞达产量:' + str(IN_9) + ';底部产量:' + str(OUT_9) + ',异常,请检查'
            mobile_list = ['179xxxxxx']
            # 发送钉钉消息
            send_dingtalk_message(access_token, content, mobile_list)

    sa10 = client.get_node('ns=2;s=SWBZ_2_PLC_10.SWBZ_2_PLC_10._System._SecondsInError')
    sa_10 = sa10.get_value()
    if sa_10 == 0:
        IN_number_10 = client.get_node('ns=2;s=SWBZ_2_PLC_10.SWBZ_2_PLC_10.飞达产量')
        IN_10 = IN_number_10.get_value()
        OUT_number_10 = client.get_node('ns=2;s=SWBZ_2_PLC_10.SWBZ_2_PLC_10.底部产量')
        OUT_10 = OUT_number_10.get_value()
        if IN_10 < OUT_10 - 200:
            content = '产量报警：10号机飞达产量:' + str(IN_10) + ';底部产量:' + str(OUT_10) + ',异常,请检查'
            mobile_list = ['1710xxxxxx']
            # 发送钉钉消息
            send_dingtalk_message(access_token, content, mobile_list)

    sa11 = client.get_node('ns=2;s=SWBZ_2_PLC_11.SWBZ_2_PLC_11._System._SecondsInError')
    sa_11 = sa11.get_value()
    if sa_11 == 0:
        IN_number_11 = client.get_node('ns=2;s=SWBZ_2_PLC_11.SWBZ_2_PLC_11.飞达产量')
        IN_11 = IN_number_11.get_value()
        OUT_number_11 = client.get_node('ns=2;s=SWBZ_2_PLC_11.SWBZ_2_PLC_11.底部产量')
        OUT_11 = OUT_number_11.get_value()
        if IN_11 < OUT_11 - 200:
            content = '产量报警：11号机飞达产量:' + str(IN_11) + ';底部产量:' + str(OUT_11) + ',异常,请检查'
            mobile_list = ['1711xxxxxx']
            # 发送钉钉消息
            send_dingtalk_message(access_token, content, mobile_list)

    sa12 = client.get_node('ns=2;s=SWBZ_2_PLC_12.SWBZ_2_PLC_12._System._SecondsInError')
    sa_12 = sa12.get_value()
    if sa_12 == 0:
        IN_number_12 = client.get_node('ns=2;s=SWBZ_2_PLC_12.SWBZ_2_PLC_12.飞达产量')
        IN_12 = IN_number_12.get_value()
        OUT_number_12 = client.get_node('ns=2;s=SWBZ_2_PLC_12.SWBZ_2_PLC_12.底部产量')
        OUT_12 = OUT_number_12.get_value()
        if IN_12 < OUT_12 - 200:
            content = '产量报警：12号机飞达产量:' + str(IN_12) + ';底部产量:' + str(OUT_12) + ',异常,请检查'
            mobile_list = ['1712xxxxxx']
            # 发送钉钉消息
            send_dingtalk_message(access_token, content, mobile_list)

    sa13 = client.get_node('ns=2;s=SWBZ_2_PLC_13.SWBZ_2_PLC_13._System._SecondsInError')
    sa_13 = sa13.get_value()
    if sa_13 == 0:
        IN_number_13 = client.get_node('ns=2;s=SWBZ_2_PLC_13.SWBZ_2_PLC_13.飞达产量')
        IN_13 = IN_number_13.get_value()
        OUT_number_13 = client.get_node('ns=2;s=SWBZ_2_PLC_13.SWBZ_2_PLC_13.底部产量')
        OUT_13 = OUT_number_13.get_value()
        if IN_13 < OUT_13 - 200:
            content = '产量报警：13号机飞达产量:' + str(IN_13) + ';底部产量:' + str(OUT_13) + ',异常,请检查'
            mobile_list = ['1713xxxxxx']
            # 发送钉钉消息
            send_dingtalk_message(access_token, content, mobile_list)

    sa14 = client.get_node('ns=2;s=SWBZ_2_PLC_14.SWBZ_2_PLC_14._System._SecondsInError')
    sa_14 = sa14.get_value()
    if sa_14 == 0:
        IN_number_14 = client.get_node('ns=2;s=SWBZ_2_PLC_14.SWBZ_2_PLC_14.飞达产量')
        IN_14 = IN_number_14.get_value()
        OUT_number_14 = client.get_node('ns=2;s=SWBZ_2_PLC_14.SWBZ_2_PLC_14.底部产量')
        OUT_14 = OUT_number_14.get_value()
        if IN_14 < OUT_14 - 200:
            content = '产量报警：14号机飞达产量:' + str(IN_14) + ';底部产量:' + str(OUT_14) + ',异常,请检查'
            mobile_list = ['1714xxxxxx']
            # 发送钉钉消息
            send_dingtalk_message(access_token, content, mobile_list)

    sa15 = client.get_node('ns=2;s=SWBZ_2_PLC_15.SWBZ_2_PLC_15._System._SecondsInError')
    sa_15 = sa15.get_value()
    if sa_15 == 0:
        IN_number_15 = client.get_node('ns=2;s=SWBZ_2_PLC_15.SWBZ_2_PLC_15.飞达产量')
        IN_15 = IN_number_15.get_value()
        OUT_number_15 = client.get_node('ns=2;s=SWBZ_2_PLC_15.SWBZ_2_PLC_15.底部产量')
        OUT_15 = OUT_number_15.get_value()
        if IN_15 < OUT_15 - 200:
            content = '产量报警：15号机飞达产量:' + str(IN_15) + ';底部产量:' + str(OUT_15) + ',异常,请检查'
            mobile_list = ['1715xxxxxx']
            # 发送钉钉消息
            send_dingtalk_message(access_token, content, mobile_list)
    time.sleep(10)
except Exception as e:
    print(e)
finally:
    client.disconnect()







