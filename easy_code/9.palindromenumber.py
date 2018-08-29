#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 9.palindromenumber.py 
@time: 2018/8/28/上午9:32
@software: PyCharm
"""

"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
Follow up:

Coud you solve it without converting the integer to a string?
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def isPalindrome(x):
    """
    :type x: int
    :rtype: bool
    """
    y = x
    if(x<0):
        return False
    ans = 0
    while(x>0):
        ans = ans*10 + x%10
        x/=10
    if(ans == y):
        return True
    else:
        return False


if __name__ == "__main__":
    print isPalindrome(10)
    pass