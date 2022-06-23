#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2022/1/4 11:18
#@Author: JiangXingGang
#@File  : SQL_FIND.py
import pymssql
conn = pymssql.connect(host='10.4.20.89', user='sa',password='sjky123+',database='SCADA',charset='UTF8')
cursor = conn.cursor()

cursor.execute('select top 10 * from SCADA.dbo.SWBZ_2_1#ZDJ')
rs = cursor.fetchall()
print(rs)