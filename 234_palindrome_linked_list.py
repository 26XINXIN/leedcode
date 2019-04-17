# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        fast, slow = head, head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        slow = self.reverse(slow)
        fast = head
        while slow is not None:
            if slow.val != fast.val:
                return False
            slow = slow.next
            fast = fast.next
        return True 
    
    def reverse(self, head):
        pre = None
        next = None
        while head is not None:
            next = head.next
            head.next = pre
            pre = head
            head = next
        return pre
        