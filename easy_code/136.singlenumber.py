#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 136.singlenumber.py 
@time: 2018/9/1/上午11:50
@software: PyCharm
"""

"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4

异或处理，这样相同的 全部都删去
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def singleNumber(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = nums[0]
    for i in range(1,nums.__len__()):
        res = res^nums[i]
    return res


if __name__ == "__main__":
    print singleNumber([2,1,3,1,3,4,5,6,5,6,4])
    pass