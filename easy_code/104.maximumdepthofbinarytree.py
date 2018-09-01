#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 104.maximumdepthofbinarytree.py 
@time: 2018/9/1/下午4:33
@software: PyCharm
"""

"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def maxDepth(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    if root is None:
        return 0
    left = maxDepth(root.left) + 1
    right = maxDepth(root.right) + 1
    if left > right:
        return left
    else:
        return right


if __name__ == "__main__":
    pass