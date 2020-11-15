import random

from models import Tpoint


class XAddress(Tpoint):
    """
    NOTE
    NOTE 此处有一个问题，生成的entry如果需要扩展(添加属性或方法)的需求, 如何处理? 例如Tpoint需要有个新字段/方法来对外表达自己有一对正确或
    NOTE 错误的经纬度.
    NOTE
    NOTE models.py文件是不允许修改的; 因为DB有可能有变化, 一旦有变化, 就需要重新生成models.py; 那么之前人工修改过的东西会全部丢失。
    NOTE 故，只能通过继承或合成的方式来扩展Entry.
    NOTE
    NOTE 此项目，我们采用继承来扩展Tpoint。
    NOTE
    """

    group_id = None
    sim = None

    # 标准地址
    std_addr = None

    # 标准地址是否新地址, 1 dicate yes, 0 indicate no, otherwise unknown.
    is_new_std_addr = None

    # true indicate stock addr, otherwise increment addr
    is_stock = False

    def __init__(self):
        super(Tpoint, self).__init__()
        self.is_new_std_addr = None

    def has_valid_lat_lng(self) -> (bool):
        try:
            (1.0 / float(self.longitude)) and (1.0 / float(self.latitude))
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
