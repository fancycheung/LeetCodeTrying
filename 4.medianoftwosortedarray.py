#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 4.medianoftwosortedarray.py 
@time: 2018/8/27/上午9:01
@software: PyCharm
"""

"""
comment here
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")

def findMedianSortedArrays(nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    nums3 = []
    i, j = 0, 0
    while (i < nums1.__len__() and j < nums2.__len__()):
        a = nums1[i]
        b = nums2[j]
        print a,b
        if a < b:
            nums3.append(a)
            i += 1
        else:
            nums3.append(b)
            j += 1
    if (i == nums1.__len__()):
        for k in range(j, nums2.__len__()):
            nums3.append(nums2[k])
    if (j == nums2.__len__()):
        for k in range(i, nums1.__len__()):
            nums3.append(nums1[k])
    length = nums3.__len__()
    print nums3
    if (length % 2 == 1):
        return nums3[(length - 1) / 2]
    else:
        a = nums3[length/2]
        b = nums3[(length - 2) / 2]
        return (a + b) * 1.0 / 2


if __name__ == "__main__":
    a = [1,3]
    b = [2]
    c = findMedianSortedArrays(a,b)
    print c
    pass