#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 167.twosumiiinputarrayissorted.py 
@time: 2018/9/1/下午2:59
@software: PyCharm
"""

"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.

思路：两个指针 ，一个从前往后，一个从后往前。一直match
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def twoSum(numbers, target):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    start, end = 0, numbers.__len__() - 1
    while start < end:
        if numbers[start] + numbers[end] > target:
            end -= 1
        elif numbers[start] + numbers[end] < target:
            start += 1
        else:
            return start + 1, end + 1


if __name__ == "__main__":
    numbers = [2, 9, 11, 15]
    target = 9
    print twoSum(numbers, target)
    pass