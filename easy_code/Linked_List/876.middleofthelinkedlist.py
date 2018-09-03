#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 876.middleofthelinkedlist.py 
@time: 2018/9/3/上午9:41
@software: PyCharm
"""

"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

 

Example 1:

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.
Example 2:

Input: [1,2,3,4,5,6]
Output: Node 4 from this list (Serialization: [4,5,6])
Since the list has two middle nodes with values 3 and 4, we return the second one.
 

Note:

The number of nodes in the given list will be between 1 and 100.
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def middleNode(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    one, two = head, head
    while two and two.next:
        one = one.next
        two = two.next.next
    return one

if __name__ == "__main__":
    pass