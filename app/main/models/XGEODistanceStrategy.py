import math
from math import pi, cos, sin
from app.main.models.XAddress import XAddress


class XGEODistanceStrategy(object):
    """
    计算两个经纬度之间的距离(python算法)
    https://www.cnblogs.com/lgh344902118/p/7490795.html
    """

    def __init__(self):
        pass

    def _rad(self, d) -> (float):
        """
        NOTE 注意public private函数的定义方式, private函数一般以下划线开头, public则无需下划线开头
        :param d:
        :return:
        """
        try:
            r = float(d) * float(pi) / float(180.0)
        except Exception as e:
            r = 1
        return r

    def compare(self, p_address_a: XAddress = None, p_address_b: XAddress = None) -> (bool, float):
        """小于等于指定距离(MIN_DISTANCE), 则认为 这两个点是同一个地址
        :param p_address_a:
        :param p_address_b:
        :return:2个地址距离是否小于200米;两点之间的真实距离(单位为米).
        """
        EARTH_REDIUS = 6378.137
        lat_diff = self._rad(p_address_a.latitude) - self._rad(p_address_b.latitude)
        lon_diff = self._rad(p_address_a.longitude) - self._rad(p_address_b.longitude)
        s = 2 * math.asin(math.sqrt(math.pow(sin(lat_diff / 2), 2) + cos(self._rad(p_address_a.latitude)) * cos(self._rad(p_address_b.latitude)) * math.pow(sin(lon_diff / 2), 2)))
        real_distance = s * EARTH_REDIUS * 1000
        rst = real_distance <= 200
        return rst, real_distance
