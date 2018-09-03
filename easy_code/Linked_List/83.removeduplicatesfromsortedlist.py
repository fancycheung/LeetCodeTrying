#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 83.removeduplicatesfromsortedlist.py 
@time: 2018/8/29/下午4:06
@software: PyCharm
"""

"""
Given a sorted linked list, delete all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2
Example 2:

Input: 1->1->2->3->3
Output: 1->2->3
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def deleteDuplicates(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None or head.next is None:
        return head

    pre, now = head, head.next
    prevalue = pre.val
    while now is not None:
        nowvalue = now.val
        if nowvalue == prevalue:
            pre.next = now.next
            del now
            now = pre.next
        else:
            pre = pre.next
            now = now.next
            prevalue = pre.val
    return head


if __name__ == "__main__":
    pass