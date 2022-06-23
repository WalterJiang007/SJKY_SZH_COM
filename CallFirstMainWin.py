#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/6/2 9:16
# @Author: JiangXingGang
# @File  : CallFirstMainWin.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

QApplication.processEvents()

from firstmainframe import *
import socket  # 导入 socket 模块
import threading
import time


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)


s = socket.socket()  # 创建 socket 对象
host = '10.3.21.26'  # 获取本地主机名
port = 51236  # 设置端口号
s.connect((host, port))
global t


def RCV():
    str1 = s.recv(50)[0:50]
    char = '#'
    str1 = str(str1)[2:-5]
    print(str1, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    str2 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    str_total = str(str1) + "  " + str(str2)
    # 查找#所在位置
    ts_pos = str1.find(char)  # 第一个#
    ts_pos_1 = str1.find(char, (ts_pos + 1))  # 第二个#
    ts_pos_2 = str1.find(char, (ts_pos_1 + 1))  # 第三个#

    # print(ts_pos)
    str_num = str1[0:ts_pos]
    # print(str_num)

    # print(ts_pos_1)
    str_num2 = str1[(ts_pos + 1):ts_pos_1]
    # print(str_num2)

    # print(ts_pos_2)
    str_num3 = str1[(ts_pos_1 + 1):ts_pos_2]
    # print(str_num3)

    str_num4 = str1[(ts_pos_2 + 1):]
    # print(str_num4)

    with open('D:\二维码数据', 'a') as f:
        f.write('\n')
        f.write('%s          %s' % (s.recv(50)[1:39], time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        f.close()

    myWin.label_5.setText(QtCore.QCoreApplication.translate("myWin.MainWindow", str_num2))
    myWin.label_6.setText(QtCore.QCoreApplication.translate("myWin.MainWindow", str_total))
    myWin.label_7.setText(QtCore.QCoreApplication.translate("myWin.MainWindow", str_num3))
    myWin.label_8.setText(QtCore.QCoreApplication.translate("myWin.MainWindow", str_num4))

    QApplication.processEvents()
    t = threading.Timer(0.3, RCV)
    t.start()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    RCV()
    app.exec()
    # sys.exit(app.exec_())
