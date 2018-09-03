#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 160.intersectionoftwolinkedlists.py 
@time: 2018/9/1/下午12:03
@software: PyCharm
"""

"""
Write a program to find the node at which the intersection of two singly linked lists begins.


For example, the following two linked lists:

A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗            
B:     b1 → b2 → b3
begin to intersect at node c1.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.

思路：取两个链表长度,先将长链表 走 长度之差的步骤，再同时走 和 比较 ，有相同则返回
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    temp = set()
    tempA = headA
    tempB = headB

    if headA and headB is None:
        return None

    while tempA:
        temp.add(tempA)
        tempA = tempA.next

    while tempB:
        if tempB in temp:
            return tempB
        tempB = tempB.next

    return None

if __name__ == "__main__":
    pass