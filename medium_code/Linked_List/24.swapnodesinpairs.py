#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 24.swapnodesinpairs.py 
@time: 2018/9/3/上午10:23
@software: PyCharm
"""

"""
Given a linked list, swap every two adjacent nodes and return its head.

Example:

Given 1->2->3->4, you should return the list as 2->1->4->3.
Note:

Your algorithm should use only constant extra space.
You may not modify the values in the list's nodes, only nodes itself may be changed.

"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def swapPairs(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    now = head
    while now and now.next:
        suff = now.next
        tmp = now.val
        now.val = suff.val
        suff.val = tmp
        now = suff.next
    return head


if __name__ == "__main__":
    pass