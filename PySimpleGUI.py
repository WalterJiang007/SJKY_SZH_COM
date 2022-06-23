#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/6/7 10:30
# @Author: JiangXingGang
# @File  : PySimpleGUI.py
import PySimpleGUI as sg

layout = [[sg.Text("测试 PySimpleGUI")], [sg.Button("OK")]]
window = sg.Window("样例", layout)
while True:
    event, values = window.read()
    if event == "OK" or event == sg.WIN_CLOSED:
        break
window.close()