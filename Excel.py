#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Time  : 2022/4/2 14:22
# @Author: JiangXingGang
# @File  : Excel.py

#How to write to an Excel using xlwt module
import xlwt
#创建一个Wordbook对象，相当于创建了一个Excel文件
book = xlwt.Workbook(encoding = "utf-8", style_compression = 0)
#创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格
sheet = book.add_sheet("sheet1", cell_overwrite_ok = True)
#向表sheet1中添加数据
sheet.write(0, 0, "EnglishName") #其中，"0, 0"指定表中的单元格，"EnglishName"是向该单元格中写入的内容
sheet.write(1, 0, "MaYi")
sheet.write(0, 1, "中文名字")
sheet.write(1, 1, "蚂蚁")
#最后，将以上操作保存到指定的Excel文件中
book.save("name.xls")

# How to read from an Excel using xlrd module
import xlrd
# 打开指定路径中的xls文件，得到book对象
xls_file = "name.xls"
#打开指定文件
book = xlrd.open_workbook(xls_file)
# 通过sheet索引获得sheet对象
sheet1 = book.sheet_by_index(0)
# # 获得指定索引的sheet名
# sheet1_name = book.sheet_names()[0]
# print(sheet1_name)
# # 通过sheet名字获得sheet对象
# sheet1 = book.sheet_by_name(sheet1_name)
# 获得行数和列数
# 总行数
nrows = sheet1.nrows
#总列数
ncols = sheet1.ncols
# 遍历打印表中的内容
for i in range(nrows):
  for j in range(ncols):
    cell_value = sheet1.cell_value(i, j)
    print(cell_value, end = "\t")
  print("")