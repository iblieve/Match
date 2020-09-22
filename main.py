#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import sys, datetime
import xlrd, xlwt
from app.main.models.XAddress import XAddress
from app.main.models.XGEODistanceStrategy import XGEODistanceStrategy
from app.utils.XUtils import XUtils


def main(p_argv):
    # excel_title = ['group_id', '序号', '地址编号', '省份', '城市', '区/县', '乡', '详细地址（拼接省市区）', '详细地址(PROD地址)', '经度', '纬度']
    excel_title = ['序号', '地址编号', '省份', '城市', '区/县', '乡', '详细地址（拼接省市区）', '详细地址(PROD地址)', '经度', '纬度']
    resource = 'resources/receiving_address_stock_1_ok.xls'
    stock_addr_list = XUtils.excel_to_list(p_read_excel_file_path=resource, p_sheet_name='Sheet1', p_excel_title_list=excel_title)
    top_10 = []
    for i in range(0, 10):
        tmp_dict = stock_addr_list[i]
        tmp_dict['group_id'] = 0
        top_10.append(tmp_dict)
        # print(tmp_dict["rowid"])
    t = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    # XUtils.dump_list_2_excel(p_title_list=excel_title_1, p_data_list=top_10, p_excel_name="top_10_{}.xls".format(t))
    x = XAddress(stock_addr_list[6])
    y = XAddress(stock_addr_list[8])
    rst, real_distance = XGEODistanceStrategy.compare(x, y)
    print(rst)
    print(real_distance)

    return 0


if __name__ == '__main__':
    start = datetime.datetime.now()

    status = main(sys.argv)

    elapsed = float((datetime.datetime.now() - start).seconds)
    print("Time Used 4 All ----->>>> %f seconds" % (elapsed))

    sys.exit(status)
