#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 86.partitionalist.py
@time: 2018/9/3/下午1:35
@software: PyCharm
"""
from medium_code.Linked_List import ListNode

"""
Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def partition(head, x):
    """
    :type head: ListNode
    :type x: int
    :rtype: ListNode
    """
    res = []
    nhead = ListNode(None)
    nhead.next = head
    pre, now = nhead, head
    while now:
        if now.val >= x:
            #del
            res.append(now.val)
            pre.next = now.next
            now = pre.next
        else:
            pre = pre.next
            now = now.next

    for item in res:
        tmp = ListNode(item)
        pre.next = tmp
        pre = pre.next
    return nhead.next


if __name__ == "__main__":
    pass