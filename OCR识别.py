#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/5/20 14:11
# @Author: JiangXingGang
# @File  : OCR识别.py

import easyocr

# 设置识别中英文两种语言
reader = easyocr.Reader(['ch_sim'], gpu=False)  # need to run only once to load model into memory
result = reader.readtext(r"d:\1.jpg")
print(result)