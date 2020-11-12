#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
import sys, datetime
import xlrd, xlwt
from app.main.models.XAddress import XAddress
from app.main.models.XGEODistanceStrategy import XGEODistanceStrategy
from app.main.models.XAddressStringDiffStrategy import XAddressStringDiffStrategy
from app.utils.XUtils import XUtils
from app.main.XConstants import XConstants
from XExport import export_excel
from XRead_data import create_list
from config import app_config, ProductionConfig, DevelopmentConfig


def main(p_argv=None):
    profile = p_argv[1] if len(p_argv) > 1 else 'dev'
    #
    config = app_config[profile]
    if os.getenv('DB_HOST') is not None:
        config.DB_HOST = os.getenv('DB_HOST')
        config.DB_PORT = os.getenv('DB_PORT')
        config.DB_USER = os.getenv('DB_USER')
        config.DB_PASSWORD = os.getenv('DB_PASSWORD')
        config.DB_INSTANCE_NAME = os.getenv('DB_INSTANCE_NAME')
        config.DB_CHARSET = os.getenv('DB_CHARSET')

    addr_list = fetch_all_address_by(p_config=config)
    top_10 = []
    for i in range(0, 10):
        tmp_dict = addr_list[i]
        tmp_dict['group_id'] = 0
        top_10.append(tmp_dict)
        # print(tmp_dict["rowid"])
    t = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    # XUtils.dump_list_2_excel(p_title_list=excel_title_1, p_data_list=top_10, p_excel_name="top_10_{}.xls".format(t))
    x = XAddress(addr_list[6])
    y = XAddress(addr_list[8])
    rst, real_distance = XGEODistanceStrategy().compare(p_address_a=x, p_address_b=y)
    print(rst)
    print(real_distance)

    # Note 总共生成两个表，算上原始表就有三个
    # Note 假如说第一个数据进来，直接就扔到第二个表里，给他一个编号1.第二个进来跟第一个比较，然后没匹配上扔到表2给他一个编号2.第三个进来了，跟前两个比较，
    # Note 假如说匹配到了1，我们给他也扔到表2里给编号1。。。这样的话表2就会有4636-150个数据，但是每一数据都有一个编号。然后在根据这个编号顺序排一下，这样就把相同的归在一起了
    # Note 这个是把相同/类似的地址 编一个相同的号，  相当于分组
    new_excel_dict_grouped = {}
    new_excel_list_grouped = []
    group_id = 0
    for tmp_dict in addr_list:

        rst, brother_dict, sim = contains(p_new_excel_list=new_excel_list_grouped, p_old_dict=tmp_dict)

        print(rst)
        print(sim)

        if rst is False:
            group_id += 1
            # 建立小组
            new_excel_dict_grouped[str(group_id)] = []
            # Note 加一列数据group_id
            tmp_dict['group_id'] = group_id
        else:
            # Note 此处要非常注意， 应该使用它兄弟的group_id, 而不是使用最新的group_id
            tmp_dict['group_id'] = brother_dict['group_id']
        new_excel_list_grouped.append(tmp_dict)
        # Note 分组, 同一小组的记录具有相同group_id
        new_excel_dict_grouped[str(tmp_dict['group_id'])].append(tmp_dict)

    # NOTE
    #

    return 0


def fetch_all_address_by(p_config=None) -> (list):
    result = create_list(p_config=p_config)
    length_sql = len(result)
    stock_addr_list = []
    for i in range(length_sql):
        stock_addr_dict = {}
        stock_addr_dict['rowid'] = result[i].row_id
        stock_addr_dict['locationId'] = result[i].location_id
        stock_addr_dict['provinceName'] = result[i].province_name
        stock_addr_dict['cityName'] = result[i].city_name
        stock_addr_dict['districtName'] = result[i].district_name
        stock_addr_dict['townName'] = result[i].town_name
        stock_addr_dict['locationName'] = result[i].location_name
        stock_addr_dict['address'] = result[i].address
        stock_addr_dict['longitude'] = result[i].longitude
        stock_addr_dict['latitude'] = result[i].latitude
        stock_addr_list.append(stock_addr_dict)
    return stock_addr_list


def contains(p_new_excel_list=None, p_old_dict=None):
    """
    判断
    :param p_new_excel_list:
    :param p_old_dict:
    :return: rst为true的时候表示能够在p_new_excel_list找到兄弟节点， 否则找不到兄弟节点。 (所谓兄弟节点就是指着这2个点认为是同一个地址), brother_dict是p_old_dict的兄弟节点.
    """
    rst = False
    max_sim = -3721.4728
    brother_dict = None

    # 竟然没有SIM ？？？？？？？？？？？？？？
    for tmp_new_dict in p_new_excel_list:

        # Note 利用余弦相似度公式计算两字符串的相似性 (相似度达到0.8则认为是一个地址，否则是2个不同地址, 这个0.8我是随便写的, 可修改)
        # rst_cos_sim = CosineSimilarityStrategy().compare(p_address_dict_a=tmp_new_dict, p_address_dict_b=p_old_dict)

        # NOTE 通过对经纬度的比较，相差百分之一或更小以内的视为同一地址，否则视为两个地址
        # rst_lal = LALPctStrategy().compare(p_address_dict_a=tmp_new_dict, p_address_dict_b=p_old_dict)

        # Note 根据距离来判断(200米)

        new_address = XAddress(tmp_new_dict)
        old_address = XAddress(p_old_dict)
        match_distance, real_distance = XGEODistanceStrategy().compare(p_address_a=new_address, p_address_b=old_address)
        # real_distance = random.randint(0, 5000000)
        # 2个点的真实距离
        x = real_distance

        # Note 计算字符匹配度
        # 详细地址（拼接省市区）匹配度; 详细地址(PROD地址) 匹配度
        # rst_str_diff, sim_string = XAddressStringDiffStrategy().compare(p_address_dict_a=new_address, p_address_dict_b=old_address)
        # sim_string = random.random()
        # a是字符串相似度, b是距离相似度
        # a = sim_string
        # NOTE 暂时强行设置字符串匹配度为1(即完全匹配), 这样可以使得流程能够正常跑通，将来再把字符串匹配算法加上。
        a = 1.0

        # 首先判断，已有地址的这一条数据有没有经纬度
        # 如果有
        #       计算距离X
        #       再计算b =（500 - X） / 500, Note 此处的500也作为一个参数，允许调整，见XConstants.FIXED_DISTANCE
        #       这里加上一个b的下限
        #       b下限 =（β - a理论 * α） / （1 - α）
        #       如果b小于这个值
        #       b直接等于这个值
        #       这一步主要保证了当a大于a理论（0.95）时，匹配一定能成功大于β（判定值）0.6
        #       α就是你的FACTER权重
        # 如果没有
        #       b = 0
        if old_address.has_valid_lat_lng:
            # if XUtils.has_valid_lat_lng(old_address):
            # 计算根据距离算出来的相似度. 其中x是求大圆算出来的距离， 即2个点的真实距离
            b = (XConstants.FIXED_DISTANCE - x) / XConstants.FIXED_DISTANCE
            # b还影响匹配度， 但是影响程度非常低
            B_MIN = (XConstants.BETA - XConstants.A_THEORY * XConstants.ALPHA) / (1 - XConstants.ALPHA)
            if b < B_MIN:
                b = B_MIN
        else:
            b = 0

        #
        sim = XConstants.ALPHA * a + (1 - XConstants.ALPHA) * b

        # rst = match_distance is True and rst_str_diff is True
        # NOTE 看这里  ...................... 此处也需要人为调整
        if rst is False:
            # 一旦匹配到一个兄弟后， 就认为成功, 后续就无需再考虑rst了， 后续就是去找匹配度更高的兄弟即可
            rst = sim >= 0.6

        tmp_new_dict['sim'] = sim

        # Note 取得sim 最大的作为兄弟返回
        if rst is True:
            if brother_dict is None or tmp_new_dict['sim'] > brother_dict['sim']:
                brother_dict = tmp_new_dict
                max_sim = brother_dict['sim']

    return rst, brother_dict, max_sim


if __name__ == '__main__':
    start = datetime.datetime.now()

    status = main(sys.argv)

    elapsed = float((datetime.datetime.now() - start).seconds)
    print("Time Used 4 All ----->>>> %f seconds" % (elapsed))

    sys.exit(status)
