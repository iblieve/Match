#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys, datetime
from app.utils.XUtils import XUtils
import xlrd, xlwt

"""
    package.module
    ~~~~~~~~~~~~~~
    舒尔特方格 25 / 36 / 49 / 64
    # 5 * 5如下， 即25个元素打乱后取值即可。
"""

import random
import os
import os.path

# form openpyxl.styles import Border, borders, colors, Side

G_N = 3
G_START_ROW_INDEX = 0


def dump_list_2_excel(workbook=None, worksheet=None, p_n=None, p_data_list=None, p_excel_name='Excel_test.xls'):
    borders = xlwt.Borders()  # Create borders

    borders.left = xlwt.Borders.THIN  # 添加边框-虚线边框
    borders.right = xlwt.Borders.THIN  # 添加边框-虚线边框
    borders.top = xlwt.Borders.THIN  # 添加边框-虚线边框
    borders.bottom = xlwt.Borders.THIN  # 添加边框-虚线边框
    borders.left_colour = 0x90  # 边框上色
    borders.right_colour = 0x90
    borders.top_colour = 0x90
    borders.bottom_colour = 0x90

    # 为样式创建字体
    font = xlwt.Font()
    # 字体类型
    font.name = 'name Times New Roman'
    # 字体颜色
    #font.colour_index = i
    # 字体大小，20为衡量单位, 32为字号，
    font.height = 20 * 32
    # 字体加粗
    font.bold = True


    row_index = G_START_ROW_INDEX
    for row_data in p_data_list:
        col_index = 0
        for value in row_data:
            style2 = xlwt.XFStyle()
            # 设置单元格对齐方式
            alignment = xlwt.Alignment()
            # 0x01(左端对齐)、0x02(水平方向上居中对齐)、0x03(右端对齐)
            alignment.horz = 0x02
            # 0x00(上端对齐)、 0x01(垂直方向上居中对齐)、0x02(底端对齐)
            alignment.vert = 0x01
            style2.alignment = alignment
            style2.borders = borders  # Add borders to style
            style2.font = font

            worksheet.write(row_index, col_index, value, style2)

            tmp_col = worksheet.col(row_index)  # xlwt中是行和列都是从0开始计算的
            if G_N == 3:
                tmp_col.width = 300 * 20
                tmp_col.height = 600
            if G_N == 4:
                tmp_col.width = 250 * 20
            if G_N == 5:
                tmp_col.width = 200 * 20
            if G_N == 6:
                tmp_col.width = 175 * 20

            col_index += 1

        tall_style = xlwt.easyxf('font:height 1800;')  # 36pt,类型小初的字号
        first_row = worksheet.row(row_index)
        first_row.set_style(tall_style)

        #worksheet.set_row(row_index, 40)  # 设置第4行高度为20

        row_index += 1
    # 保存
    # workbook.save(p_excel_name)
    return workbook


def schulte(n):
    '''return n*n'''

    excel_data_2d = []

    # 打乱数字
    max = n * n
    numbers = list(range(1, max + 1))  # 兼容py3
    random.shuffle(numbers)

    i = 0
    while i < max:
        row_data = []
        for x in numbers[i: i + n]:
            row_data.append(x)
        i += n
        excel_data_2d.append(row_data)

    return excel_data_2d, row_data


import xlwt

# 创建一个workbook 设置编码
workbook = xlwt.Workbook(encoding='utf-8')
# 创建一个worksheet
worksheet = workbook.add_sheet('sheet1')

for i in range(0, 2):
    G_START_ROW_INDEX = (G_N + 10) * i

    excel_data, top_10 = schulte(G_N)
    t = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    workbook = dump_list_2_excel(workbook=workbook, worksheet=worksheet, p_n=i, p_data_list=excel_data, p_excel_name="{}.xls".format(G_N))

p_excel_name = "{}.xls".format(G_N)
if os.path.exists(p_excel_name):
    os.remove(p_excel_name)
workbook.save(p_excel_name)
