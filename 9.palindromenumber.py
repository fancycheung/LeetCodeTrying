#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 9.palindromenumber.py 
@time: 2018/8/28/上午9:32
@software: PyCharm
"""

"""
判断整数是否为回文数字
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    y = x
    if(x<0):
        return False
    ans = 0
    while(x>0):
        ans = ans*10 + x%10
        x/=10
    if(ans == y):
        return True
    else:
        return False


if __name__ == "__main__":
    print isPalindrome(10)
    pass