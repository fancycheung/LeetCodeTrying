#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 328.oddevenlinkedlist.py 
@time: 2018/9/4/上午9:03
@software: PyCharm
"""
from medium_code.Linked_List import ListNode

"""
Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.

Example 1:

Input: 1->2->3->4->5->NULL
Output: 1->3->5->2->4->NULL
Example 2:

Input: 2->1->3->5->6->4->7->NULL
Output: 2->3->6->7->1->5->4->NULL
Note:

The relative order inside both the even and odd groups should remain as it was in the input.
The first node is considered odd, the second node even and so on ...

维护一个头指针，当
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


def oddEvenList(head):
    """
    :type head: ListNode
    :rtype: ListNode
    """
    if head is None:
        return None
    elif head.next is None or head.next.next is None:
        return head

    nhead = ListNode(None)
    nhead.next = head
    ehead = ListNode(None)#偶数的结点保存

    pre, odd, even = nhead, nhead.next, ehead
    count = 0
    while odd:
        count += 1

        if count % 2 == 0:
            pre.next = odd.next#后移一个节点

            odd.next = None#将当前结点保存在新链表中，这里一定要将需要换位的结点的next更新为none，不然会保存后续所有结点
            even.next = odd
            even = even.next

            odd = pre.next#更新临时变量
        else:
            pre = pre.next
            odd = odd.next

    pre.next = ehead.next
    return nhead.next


if __name__ == "__main__":
    head = ListNode(None)
    now = head
    for i in range(1, 6):
        print i
        tmp = ListNode(i)
        now.next = tmp
        now = now.next
    res = oddEvenList(head.next)

    while res:
        print "res:", res.val
        res = res.next
    pass