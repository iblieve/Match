#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from app.main.base.XAtomicInteger import XAtomicInteger
from app.utils.XUtils import XUtils


class XConstants(object):
    G_DIGIT_DICT = {'零': 0, '一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9}

    # 当a大于a理论（0.95）时，匹配一定能成功大于β（判定值）0.6
    A_THEORY = 0.95

    # Note 看这里 ................................... ALPHA、BETA系数, 可以调. 因为字符串匹配更优, 所以权重大一些, 此处需要人工去调
    ALPHA = 0.75
    #
    BETA = 0.8

    # 我的意思是加一个Beta2 = 0.8，sim2 = (1 + sim) / 2
    # 因为0.6有点小看着不专业，0.8看着专业一点
    # BETA2_RED_LINE = 0.8

    # 再计算b =（500 - X） / 500, Note 此处的500也作为一个参数，允许调整，见XConstants.FIXED_DISTANCE
    FIXED_DISTANCE = 500

    RGE = 0.6


    app = None
    PROFILE = None
    G_RELOAD_COUNTER = XAtomicInteger(0)
    G_DEBUG_INFO = XUtils.get_debug_info()

    FOO_BAR = '......................................'
