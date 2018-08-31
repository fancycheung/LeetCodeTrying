#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
@author:nali 
@file: 1o1.symmetrictree.py 
@time: 2018/8/31/上午9:36
@software: PyCharm
"""

"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.

"""

import sys

reload(sys)
sys.setdefaultencoding("utf8")


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def isSymmetric(root):
    """
    :type root: TreeNode
    :rtype: bool
    """


def inOrderTraversal(root, list_):
    """
    中序遍历
    :param root:
    :param list_:
    :return:
    """
    

if __name__ == "__main__":
    pass