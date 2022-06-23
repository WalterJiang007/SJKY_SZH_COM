#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/6/7 10:28
# @Author: JiangXingGang
# @File  : WxPython.py
import wxpip

myapp = wx.App()
init_frame = wx.Frame(parent=None, title='WxPython 窗口')

init_frame.Show()
myapp.MainLoop()