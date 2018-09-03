#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 61.rotatelist.py 
@time: 2018/9/3/上午11:19
@software: PyCharm
"""
from medium_code.Linked_List import ListNode

"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation:
rotate 1 steps to the right: 5->1->2->3->4->NULL
rotate 2 steps to the right: 4->5->1->2->3->NULL
Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL
放到列表里，翻转之后创建新链表
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def rotateRight(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if k == 0:
        return head
    if head is None:
        return head
    if head.next is None:
        return head

    now = head
    lis = []
    while now:
        lis.append(now.val)
        now = now.next
    length = lis.__len__()
    k = length - k % length
    lis = lis[k:] + lis[:k]

    nhead = ListNode(None)
    now = nhead
    for item in lis:
        tmp = ListNode(item)
        now.next = tmp
        now = now.next
    return nhead.next


if __name__ == "__main__":
    pass