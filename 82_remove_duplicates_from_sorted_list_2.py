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
        header = ListNode(-1)
        header.next = head
        pre = header
        it = head
        while it:
            if it.next and it.val == it.next.val:
                value = it.val
                while it and it.val == value:
                    it = it.next
            else:
                pre.next = it
                pre = it
                it = it.next
        pre.next = None
        return header.next