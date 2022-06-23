#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/6/7 10:11
# @Author: JiangXingGang
# @File  : Kivy.py
from kivy.app import App
from kivy.uix.button import Button
import socket  # 导入 socket 模块
import threading
import time

s = socket.socket()  # 创建 socket 对象
host = '10.3.10.142'  # 获取本地主机名
port = 51236  # 设置端口号
s.connect((host, port))  # 建立链接
#
#
# class EwmApp(App):
#
#     def build(self):
#         str1 = s.recv(50)[1:39]
#         print(str1, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#         with open('D:\二维码数据', 'a') as f:
#             f.write('\n')
#             f.write('%s          %s' % (s.recv(50)[1:39], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
#             f.close()
#
#         return Button(text=str(str1))
#
#
# EwmApp().run()
from kivy.app import App
from kivy.uix.button import Button

class TestApp(App):
    def build(self):
        return Button(text=" Hello Kivy World ")

TestApp().run()