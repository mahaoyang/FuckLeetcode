# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from copy import deepcopy


class Solution:

    # 返回ListNode
    def reverseList(self, node):
        # write code here
        if not node or not node.next:
            return node
        prev = None
        while node:
            tmp = node.next
            node.next = prev
            prev = node
            node = tmp
        return prev
