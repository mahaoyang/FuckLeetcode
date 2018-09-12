# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        l = []
        while head:
            l.append(head)
            head = head.next
        if len(l) < k or k < 1:
            return None
        return l[-k]

# 遍历完链表，遍历的同时缓存下头，最后依据长度输出第 -k个或none
