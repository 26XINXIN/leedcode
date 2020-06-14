# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        odd, even = head, head.next
        even_head = even
        if even is None:
            return head
        
        while even is not None:
            next_odd = self.jump_two_steps(odd)
            next_even = self.jump_two_steps(even)
            odd.next = next_odd
            even.next = next_even
            even = next_even
            if next_odd is not None:
                odd = next_odd
        odd.next = even_head
        return head
    
    def jump_two_steps(self, node):
        if node is None or node.next is None:
            return None
        return node.next.next
        