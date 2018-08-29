#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 28.implementstrstr.py 
@time: 2018/8/29/下午2:22
@software: PyCharm
"""

"""
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def strStr(haystack, needle):
    """
    :type haystack: str
    :type needle: str
    :rtype: int
    """
    len1 = len(haystack)
    len2 = len(needle)
    if len2 == 0:
        return 0
    #if haystack == needle:
    #    return 0
    lis = []
    for i in range(0, len1 - len2 + 1):
        sub = haystack[i:(i + len2)]
        lis.append(sub)
    flag = -1
    for i in range(lis.__len__()):
        if lis[i] == needle:
            flag = i
            return flag
    return flag


if __name__ == "__main__":
    print strStr("a", "a")
    pass