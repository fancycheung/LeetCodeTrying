#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 35.searchinsertposition.py 
@time: 2018/8/29/下午2:39
@software: PyCharm
"""

"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    if nums.__len__() == 0:
        return 0
    if nums.__len__() == 1:
        if target > nums[0]:
            return 1
        else:
            return 0
    idx = 0
    length = nums.__len__()
    if target <= nums[0]:
        return 0
    elif target > nums[length-1]:
        return length
    else:
        for i in range(0, length - 1):
            if target > nums[i] and target <= nums[i + 1]:
                return i + 1


if __name__ == "__main__":
    print searchInsert([1,3,5,6], 7)
    pass