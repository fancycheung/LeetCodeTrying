#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 26.removeduplicatesfromsortedarray.py 
@time: 2018/8/29/上午9:29
@software: PyCharm
"""

"""
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
Example 2:

Given nums = [0,0,1,1,1,2,2,3,3,4],

Your function should return length = 5, with the first five elements of nums being modified to 0, 1, 2, 3, and 4 respectively.

It doesn't matter what values are set beyond the returned length.
Clarification:

Confused why the returned value is an integer but your answer is an array?

Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.

Internally you can think of this:

// nums is passed in by reference. (i.e., without making a copy)
int len = removeDuplicates(nums);

// any modification to nums in your function would be known by the caller.
// using the length returned by your function, it prints the first len elements.
for (int i = 0; i < len; i++) {
    print(nums[i]);
}

这题有意思的点是 不仅要返回列表中的不同字符的个数，对于原列表 也要修改掉
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if nums.__len__() < 1:
        return 0
    if nums.__len__() == 1:
        return 1
    cnt = 1
    length = nums.__len__()
    i = 1
    while(i<length):
        try:
            if nums[i] == nums[i-1]:
                del(nums[i])
                #i -= 1
            else:
                i += 1
        except:
            break
    return nums.__len__()


if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    print removeDuplicates(nums)
    pass