#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 14.longestcommonprefix.py 
@time: 2018/8/28/上午10:49
@software: PyCharm
"""

"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.


"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    if(strs.__len__()<1):
        return ""
    max_len = len(strs[0])
    prefix = strs[0]
    for s in strs:
        length = len(s)
        if(length < max_len):
            max_len = length
            prefix = s
    while(max_len>0):
        if all(prefix in i[:max_len] for i in strs):
            return prefix
        else:
            prefix = prefix[:-1]
            max_len = len(prefix)
    if(max_len == 0):
        return ""


if __name__ == "__main__":
    print longestCommonPrefix(["dog","racecar","car"])
    pass