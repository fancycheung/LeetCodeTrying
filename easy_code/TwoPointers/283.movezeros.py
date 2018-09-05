#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 283.movezeros.py 
@time: 2018/9/4/下午5:26
@software: PyCharm
"""

"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
Note:

You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    count = 0
    i = 0
    while(i < nums.__len__()):
        try:
            if nums[i] == 0:
                del nums[i]
                count += 1
                i -= 1
            else:
                i += 1
        except:
            break
    nums.extend([0] * count)
    print nums


if __name__ == "__main__":
    nums = [0,1,1]
    moveZeroes(nums)
    pass