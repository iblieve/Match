#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys, datetime
import xlrd


def read_excel():
    wb = xlrd.open_workbook('resource/receiving_address_stock_1_ok.xls')  # 打开Excel文件
    sheet = wb.sheet_by_name('Sheet1')  # 通过excel表格名称(rank)获取工作表
    dat = []  # 创建空list
    for a in range(1, sheet.nrows):  # 循环读取表格内容（每次读取一行数据）
        cells = sheet.row_values(a)  # 每行数据赋值给cells
        data = str(cells[1])  # 因为表内可能存在多列数据，0代表第一列数据，1代表第二列，以此类推
        dat.append(data)  # 把每次循环读取的数据插入到list
    return dat


def main(p_argv):
    try:
        address_num = read_excel()  # 返回整个函数的值
        for i in range(0, 10):  # 循环读取a变量list
            print(address_num[i])
        return 0
    except FileNotFoundError:
        print("Error: 没有找到文件或读取文件失败")


if __name__ == '__main__':
    start = datetime.datetime.now()

    status = main(sys.argv)

    elapsed = float((datetime.datetime.now() - start).seconds)
    print("Time Used 4 All ----->>>> %f seconds" % (elapsed))

    sys.exit(status)
