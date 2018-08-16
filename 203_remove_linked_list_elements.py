# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        it = head
        jt = None
        while it:
            if it.val == val:
                if jt == None:
                    head = head.next
                else:
                    jt.next = it.next
            else:
                jt = it
            it = it.next
        return head
                    