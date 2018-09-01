#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 206.reverselinkedlist.py 
@time: 2018/9/1/下午5:34
@software: PyCharm
"""

"""
Reverse a singly linked list.

Example:

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
Follow up:

A linked list can be reversed either iteratively or recursively. Could you implement both?


"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def reverseList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    lis = []
    p = head
    while p is not None:
        lis.append(p.val)
        p = p.next

    nhead = ListNode(None)
    p = nhead
    for i in range(lis.__len__() - 1, -1, -1):
        tmp = ListNode(lis[i])
        p.next = tmp
        p = p.next
    return nhead.next


if __name__ == "__main__":
    pass