#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 23.mergeksortedlists.py 
@time: 2018/9/4/上午9:41
@software: PyCharm
"""
from hard_code.Linked_List import ListNode

"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def mergeKLists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    lis = []
    for tmp in lists:
        while tmp:
            lis.append(tmp.val)
            tmp = tmp.next
    lis.sort()
    nhead = ListNode(None)
    now = nhead
    for item in lis:
        tmp = ListNode(item)
        now.next = tmp
        now = now.next

    return nhead.next


if __name__ == "__main__":
    pass