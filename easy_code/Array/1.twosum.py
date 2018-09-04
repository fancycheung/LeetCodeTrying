#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 1.twosum.py 
@time: 2018/8/28/上午10:34
@software: PyCharm
"""

"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    index1, index2 = 0, 0
    dict_ = dict()
    for index, num in enumerate(nums):
        dict_[num] = index
    for index, num in enumerate(nums):
        diff = target - num
        indexNew = dict_.get(diff, 0)
        if indexNew == index:
            continue
        if indexNew:
            index1 = index
            index2 = indexNew
            break
    return (index1, index2)


if __name__ == "__main__":
    pass