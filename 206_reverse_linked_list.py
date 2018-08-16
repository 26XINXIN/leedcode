# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        it = head; jt = head.next
        it.next = None
        while jt:
            tmp = it
            it = jt
            jt = jt.next
            it.next = tmp
        return it