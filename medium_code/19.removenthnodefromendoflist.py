#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 19.removenthnodefromendoflist.py 
@time: 2018/8/30/下午2:19
@software: PyCharm
"""

"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.

Follow up:

Could you do this in one pass?

首先第一个指针移动n个位置
再第二个指针从头，一二指针一起移动，这样 第一个指针到达尾结点时，第二个指针正好处于倒数n个位置
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def removeNthFromEnd(head, n):
    """
    :type head: ListNode
    :type n: int
    :rtype: ListNode
    """
    nhead = ListNode(None)
    nhead.next = head
    pre, now , suff = nhead, head, head
    while(n>0):
        n -= 1
        suff = suff.next
    while suff is not None:
        pre = pre.next
        now = now.next
        suff = suff.next
    #del
    pre.next = now.next
    del now
    return nhead.next


if __name__ == "__main__":
    head = ListNode(1)
    res = removeNthFromEnd(head, 1)
    print res
    pass