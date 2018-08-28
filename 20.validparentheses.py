#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 20.validparentheses.py 
@time: 2018/8/28/上午11:10
@software: PyCharm
"""

"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if(len(s)%2 == 1):
        return False
    s = [i for i in s]
    dict_ = {"]": "[", "}": "{", ")": "("}
    stack = []
    for i in s:
        if i in dict_.values():
            stack.append(i)
        elif i in dict_.keys():
            if stack == [] or dict_[i] != stack.pop():
                return False
        else:
            return False
    return stack == []


if __name__ == "__main__":
    print isValid("{[}]")
    pass