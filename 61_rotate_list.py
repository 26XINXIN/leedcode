# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return None
        elif head.next == None or k == 0:
            return head

        size = 1
        last = head
        while last.next:
            size += 1
            last = last.next
        k %= size
        if k == 0:
            return head
        
        it = head
        for _ in range(size - k - 1):
            it = it.next
        
        new_head = it.next
        it.next = None
        last.next = head
        return new_head
        