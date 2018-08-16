# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        target = head.next
        head.next = None
        while target:
            it = head
            insertion = None
            while it and it.val < target.val:
                insertion = it
                it = it.next

            next_target = target.next

            if insertion == None:
                target.next = head
                head = target
            else:
                target.next = insertion.next
                insertion.next = target
            
            target = next_target
        
        return head