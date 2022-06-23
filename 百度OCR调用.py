#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/5/20 14:38
# @Author: JiangXingGang
# @File  : 百度OCR调用.py

from aip import AipOcr

APP_ID = '26279292'
API_KEY = 'ATEnUqz2e4ulSPkXIfOq62qA'
SECRET_KEY = 'yH3pBQO5SxGp4YS60Iq1HGrcEqqD49d1'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content("d:\\ABB17414-28A3-4efb-BCD8-B50AB45016F4.png")
""" 调用通用文字识别, 图片参数为本地图片 """
result = client.basicGeneral(image)
print(result)
