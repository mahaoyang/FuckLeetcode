class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(self.val)


class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)

a1.next = a2
a2.next = a3
