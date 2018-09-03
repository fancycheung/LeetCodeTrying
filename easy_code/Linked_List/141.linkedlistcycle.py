#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 141.linkedlistcycle.py 
@time: 2018/9/1/上午10:45
@software: PyCharm
"""

"""
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

两个指针 一个走一步，一个走两步: 两个汇合了 则表示有环 。否则两步的 到底了 则无环
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def hasCycle(head):
    """
    :type head: ListNode
    :rtype: bool
    """
    one, two = head, head
    if head is None or head.next is None or head.next.next is None:
        return False
    flag = False
    while(two is not None and two.next is not None and two.next.next is not None):
        one = one.next
        if two.next is None:
            flag = False
            break
        two = two.next.next
        if one == two:
            flag = True
            break
    return flag


if __name__ == "__main__":
    pass