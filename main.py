#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys, datetime
import xlrd, xlwt
from XAddress import XAddress

from app.utils.XUtils import XUtils


#
# def read_excel():
#     wb = xlrd.open_workbook('resources/receiving_address_stock_1_ok.xls')  # 打开Excel文件
#     sheet = wb.sheet_by_name('Sheet1')  # 通过excel表格名称(rank)获取工作表
#     dat = []  # 创建空list
#     for a in range(1, sheet.nrows):  # 循环读取表格内容（每次读取一行数据）
#         cells = sheet.row_values(a)  # 每行数据赋值给cells
#         data = str(cells[1])  # 因为表内可能存在多列数据，0代表第一列数据，1代表第二列，以此类推
#         dat.append(data)  # 把每次循环读取的数据插入到list
#     return dat


def main(p_argv):
    # try:
        # address_num = read_excel()  # 返回整个函数的值
        # for i in range(0, 10):  # 循环读取a变量list
        #     #print(address_num[i])
        #     pass



    #     return 0
    # except FileNotFoundError:
    #     print("Error: 没有找到文件或读取文件失败")

    excel_title = ['group_id', '序号', '地址编号', '省份', '城市', '区/县', '乡', '详细地址（拼接省市区）', '详细地址(PROD地址)', '经度', '纬度']
    excel_title_1 = ['序号', '地址编号', '省份', '城市', '区/县', '乡', '详细地址（拼接省市区）', '详细地址(PROD地址)', '经度', '纬度']
    resource = 'resources/receiving_address_stock_1_ok.xls'
    stock_addr_list = XUtils.excel_to_list(p_read_excel_file_path=resource, p_sheet_name='Sheet1', p_excel_title_list=excel_title)
    top_10 = []
    for i in range(0, 10):
        top_10.append(stock_addr_list[i])
        print(stock_addr_list[i]["rowid"])
    t = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    # XUtils.dump_list_2_excel(p_title_list=excel_title_1, p_data_list=top_10, p_excel_name="top_10_{}.xls".format(t))
    x = XAddress(stock_addr_list[21])
    print(x.longitude)



    ## NOTE pseudo code as below:
    # from app.main.models.XAddress import XAddress
    # address = XAddress(p_dict=top_10[0])
    # print(address.longitude)
    # mydict = address.serialize()
    #
    return True
    # print(top_10)
    # print(len(stock_addr_list))

    # TODO please print the top-10 rowid

    return 0


if __name__ == '__main__':
    start = datetime.datetime.now()

    status = main(sys.argv)

    elapsed = float((datetime.datetime.now() - start).seconds)
    print("Time Used 4 All ----->>>> %f seconds" % (elapsed))

    sys.exit(status)
