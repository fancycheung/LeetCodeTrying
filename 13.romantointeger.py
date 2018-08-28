#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 13.romantointeger.py 
@time: 2018/8/28/上午10:13
@software: PyCharm
"""

"""
罗马符号转为数字。这个比较简单
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    dict_ = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "O": 4, "P": 9, "Q": 40, "R": 90, "S": 400, "T": 900}
    s = s.replace("IV","O").replace("IX","P").replace("XL","Q").replace("XC","R").replace("CD","S").replace("CM","T")
    ret = 0
    s = [i for i in s]
    for st in s:
        ret += dict_[st]
    return ret


if __name__ == "__main__":
    print romanToInt("MCMXCIV")
    pass