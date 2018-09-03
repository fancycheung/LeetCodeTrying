#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 92.reverselinkedlistII.py 
@time: 2018/9/3/下午1:52
@software: PyCharm
"""
from medium_code.Linked_List import ListNode

"""
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 ≤ m ≤ n ≤ length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def reverseBetween(head, m, n):
    """
    :type head: ListNode
    :type m: int
    :type n: int
    :rtype: ListNode
    """
    if m == n:
        return head

    nhead = ListNode(None)
    nhead.next = head
    count = 0
    now = nhead
    flag = None
    stack = []
    while now:
        now = now.next
        count += 1
        if count == m:
            flag = now
            stack.append(now.val)
        elif count > m and count <= n:
            stack.append(now.val)
        elif count > m:
            break

    for i in range(stack.__len__() - 1, -1, -1):
        flag.val = stack[i]
        flag = flag.next
    return nhead.next


if __name__ == "__main__":
    pass