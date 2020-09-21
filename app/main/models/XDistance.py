import math
from math import pi, cos, sin
from app.main.models.XAddress import XAddress


def rad(d):
    return (d * pi) / 180.0


class XGEODistanceStrategy(object):
    """
    计算两个经纬度之间的距离(python算法)
    https://www.cnblogs.com/lgh344902118/p/7490795.html
    """

    # def __init__(self):
    #     pass

    @staticmethod
    def compare(p_address_a:XAddress=None, p_address_b:XAddress=None) -> (bool, float):
        """小于等于指定距离(MIN_DISTANCE), 则认为 这两个点是同一个地址
        :param p_address_a:
        :param p_address_b:
        :return:2个地址距离是否小于200米;两点之间的真实距离(单位为米).
        """
        EARTH_REDIUS = 6378.137
        lat_diff = rad(p_address_a.longitude) - rad(p_address_b.longitude)
        lon_diff = rad(p_address_a.full_name_prod) - rad(p_address_b.full_name_prod)
        s = 2 * math.asin(math.sqrt(math.pow(sin(lat_diff / 2), 2) + cos(rad(p_address_a.longitude)) * cos(rad(p_address_b.longitude)) * math.pow(sin(lon_diff / 2), 2)))
        real_distance = s * EARTH_REDIUS * 1000
        rst = real_distance <= 200
        return rst, real_distance


