# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = head
        it = head.next
        while it:
            if it.val == pre.val:
                pass
            else:
                pre.next = it
                pre = pre.next
            it = it.next
        pre.next = None
        return head