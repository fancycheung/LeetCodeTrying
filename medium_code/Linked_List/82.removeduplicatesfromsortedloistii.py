#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 82.removeduplicatesfromsortedloistii.py
@time: 2018/8/29/下午5:57
@software: PyCharm
"""
from medium_code.Linked_List import ListNode

"""
Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3

注意头结点 如果头结点就是重复的 则头结点后移
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

    nhead = ListNode(None)
    nhead.next = head
    del_list = []

    pre, now, suff = nhead, head, head.next
    while suff is not None:
        nowvalue = now.val
        suffvalue = suff.val
        if nowvalue == suffvalue or nowvalue in del_list:
            pre.next = suff
            del_list.append(nowvalue)
            del now
            now = suff
            suff = now.next
        else:
            pre = pre.next
            now = now.next
            suff = suff.next
    #最后一个节点的处理
    if now is not None and now.next is None:
        if now.val in del_list:
            pre.next = None
            del now

    return nhead.next

if __name__ == "__main__":
    pass