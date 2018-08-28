#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 7.reverseinteger.py 
@time: 2018/8/28/上午9:11
@software: PyCharm
"""

"""
整型翻转
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    flag = 0
    if x < 0:
        flag = 1
    x = abs(x)
    lis = []
    while(x>0):
        res = x%10
        x = x/10
        lis.append(res)
    if (x>0):
        lis.append(x%10)
    length = lis.__len__()
    result = 0
    for i in range(length):
        result += lis[i] * 10 ** (length - 1 - i)
    if flag == 1:
        result = -result
    if (result > 2 ** 31 - 1 or result < -2 ** 31):
        result = 0
    return result


if __name__ == "__main__":
    print reverse(-1230)
    pass