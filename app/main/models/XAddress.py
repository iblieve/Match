import random


class XAddress(object):
    order = -1
    address_no = -1
    district_code = -1
    # 省,市,区/县,乡镇
    province_name = None
    city_name = None
    district_name = None
    town_name = None

    # 详细地址（拼接省市区）
    full_name = None

    # 详细地址(PROD地址)
    full_name_prod = None

    # 经度, 纬度
    longitude = -1
    latitude = -1
    has_valid_lat_lng = True

    # 标准地址
    std_addr = None

    # 标准地址是否新地址, 1 dicate yes, 0 indicate no, otherwise unknown.
    is_new_std_addr = None

    # true indicate stock addr, otherwise increment addr
    is_stock = False

    __is_valid_data__ = True
    __message__ = None

    # 北极与南极的纬度
    south_pole_longtitude = '90S'
    north_pole_longtitude = '90N'

    def __init__(self, p_dict: dict = None):
        # ['序号', '地址编号', '省份', '城市', '区/县', '乡', '详细地址（拼接省市区）', '详细地址(PROD地址)', '经度', '纬度', '标准地址', '标准地址是否新地址']
        # 省,市,区/县,乡镇
        self.province_code = -1
        self.province_name = p_dict['provinceName']
        self.city_code = -1
        self.city_name = p_dict['cityName']
        self.district_code = p_dict['rowid']
        self.district_name = p_dict['districtName']
        self.town_code = -1
        self.town_name = p_dict['townName']
        # 经度, 纬度
        self.longitude = p_dict['longitude']
        self.latitude = p_dict['latitude']
        self.has_valid_lat_lng = self._has_valid_lat_lng(p_longitude=self.longitude, p_latitude=self.latitude)
        self.full_name = p_dict['locationName']
        self.full_name_prod = p_dict['address']

    def _has_valid_lat_lng(self, p_longitude=None, p_latitude=None) -> (bool):
        try:
            (1.0 / p_longitude) and (1.0 / p_latitude)
            ok = True
        except Exception as e:
            ok = False
        return ok

    def serialize(self) -> (dict):
        return self.__dict__

    def is_north_or_south(self):
        x = random.randint(0, 10)
        if x % 2 == 0:
            print("该地址在南半球")
        else:
            print("该地址在北半球")
