# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result = ListNode(-1)
        current = result
        next = 0
        while l1 != None and l2 != None:
            this_bit, new_next = self.half_adder(l1.val, l2.val)
            this_bit, new_next_add = self.half_adder(this_bit, next)
            next = new_next + new_next_add
            current.next = ListNode(this_bit)
            current = current.next
            l1 = l1.next
            l2 = l2.next

        if l1 == None:
            l = l2
        else:
            l = l1

        if l == None:
            if next != 0:
                current.next = ListNode(next)
                return result.next
            else:
                return result.next
        else:
            while l != None:
                this_bit, next = self.half_adder(l.val, next)
                current.next = ListNode(this_bit)
                l = l.next
                current = current.next
            if next != 0:
                current.next = ListNode(next)
                return result.next
            else:
                return result.next

    def half_adder(self, v1, v2):
        r = v1 + v2
        return r % 10, r // 10
