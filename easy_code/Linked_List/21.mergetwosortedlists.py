#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 21.mergetwosortedlists.py 
@time: 2018/8/29/上午8:51
@software: PyCharm
"""
from easy_code.Linked_List import ListNode

"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


import sys
reload(sys)
sys.setdefaultencoding("utf8")


def mergeTwoLists(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if l1 is None:
        return l2
    if l2 is None:
        return l1

    l3 = ListNode(0)
    p1,p2,p3 = l1,l2,l3
    while(p1 is not None and p2 is not None):
        v1 = p1.val
        v2 = p2.val
        tmp = ListNode(0)
        if(v1<v2):
            tmp.val = v1
            p3.next = tmp
            p3 = p3.next
            p1 = p1.next
        else:
            tmp.val = v2
            p3.next = tmp
            p3 = p3.next
            p2 = p2.next

    if p1 is not None:
        while p1 is not None:
            tmp = ListNode(0)
            tmp.val = p1.val
            p3.next = tmp
            p3 = p3.next
            p1 = p1.next

    if p2 is not None:
        while p2 is not None:
            tmp = ListNode(0)
            tmp.val = p2.val
            p3.next = tmp
            p3 = p3.next
            p2 = p2.next
    return l3.next


if __name__ == "__main__":
    pass