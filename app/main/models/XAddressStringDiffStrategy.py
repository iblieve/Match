import math
import difflib
from math import pi, cos, sin
from app.main.models.XAddress import XAddress


class XAddressStringDiffStrategy(object):
    """
    """

    def __init__(self):
        pass

    def compare(self, p_address_a: XAddress = None, p_address_b: XAddress = None) -> (bool, float):
        """
        :param p_address_a:
        :param p_address_b:
        :return:
        """
        # rst_str_diff = 1.0
        # sim_string = 1.0
        addr_1 = p_address_a.address
        addr_2 = p_address_b.address
        seq = difflib.SequenceMatcher(lambda x: x in ' ,。-()《》省市区', addr_1, addr_2)
        sim_string = seq.ratio()
        if sim_string > 0.8:
            rst_str_diff = True
        elif sim_string < 0.6:
            rst_str_diff = False
        else:
            rst_str_diff = '待定'

        # NOTE your code goes here ........

        return rst_str_diff, sim_string
