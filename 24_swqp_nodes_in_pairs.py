# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if head == None or head.next == None:
            return head
        else:
            first = head
            second = head.next
            head = second
            while first != None and second != None:
                if second.next != None and second.next.next != None:
                    first.next = second.next.next
                else:
                    first.next = second.next
                third = second.next
                second.next = first
                first = third
                if first != None:
                    second = first.next
            return head
