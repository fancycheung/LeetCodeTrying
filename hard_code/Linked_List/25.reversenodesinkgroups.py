#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 25.reversenodesinkgroups.py 
@time: 2018/9/4/上午9:43
@software: PyCharm
"""
from hard_code.Linked_List import ListNode

"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:

Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

Note:

Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def reverseKGroup(head, k):
    """
    :type head: ListNode
    :type k: int
    :rtype: ListNode
    """
    if k == 0 or head is None:
        return head
    lis = []
    count = 0
    now = head

    result = ListNode(None)
    res = result

    while now:
        count += 1
        if count == k:
            lis.append(now.val)
            print lis
            for i in range(lis.__len__()-1, -1, -1):
                tmp = ListNode(lis[i])
                res.next = tmp
                res = res.next
            lis = []
            count = 0
            now = now.next
        else:
            lis.append(now.val)
            now = now.next
    if lis.__len__() > 0:
        for item in lis:
            tmp = ListNode(item)
            res.next = tmp
            res = res.next
    return result.next


if __name__ == "__main__":
    root = ListNode(None)
    now = root
    for i in range(1, 6):
        print i
        tmp = ListNode(i)
        now.next = tmp
        now = now.next
    res = reverseKGroup(root.next, 2)
    while res:
        print "res:",res.val
        res = res.next
    pass