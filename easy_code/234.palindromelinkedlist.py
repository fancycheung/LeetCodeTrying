#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 234.palindromelinkedlist.py 
@time: 2018/9/3/上午9:00
@software: PyCharm
"""

"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
Example 2:

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
遍历两次 一次逐个入栈，一次逐个判断
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def isPalindrome(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    now = head
    stack = []
    while now:
        stack.append(now.val)
        now = now.next
    now = head
    while now:
        if now.val != stack.pop():
            return False
        now = now.next
    return True

if __name__ == "__main__":
    pass