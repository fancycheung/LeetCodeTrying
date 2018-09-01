#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 203.removelinkedlistelements.py 
@time: 2018/9/1/下午5:09
@software: PyCharm
"""

"""
Remove all elements from a linked list of integers that have value val.

Example:

Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5

"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def removeElements(head, val):
    """
    :type head: ListNode
    :type val: int
    :rtype: ListNode
    """
    if head is None:
        return head
    nhead = ListNode(None)
    nhead.next = head
    pre, now = nhead, head
    while now is not None:
        if now.val == val:
            pre.next = now.next
            del now
            now = pre.next
        else:
            now = now.next
            pre = pre.next
    return nhead.next


if __name__ == "__main__":
    pass