#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 66.plusone.py 
@time: 2018/8/30/上午9:40
@software: PyCharm
"""

"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def plusOne(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    result = [0] + digits
    flag = 1
    for i in range(result.__len__() - 1, -1, -1):
        value = result[i] + flag
        flag = value/10
        value = value%10
        result[i] = value
    if result[0] == 0:
        return result[1:]
    else:
        return result


if __name__ == "__main__":
    a = [9,9,9,9]
    print plusOne(a)
    pass