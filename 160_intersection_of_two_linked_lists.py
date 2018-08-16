# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        n1 = 0
        n2 = 0
        it = headA
        while it:
            n1 += 1
            it = it.next
        it = headB
        while it:
            n2 += 1
            it = it.next
        it = headA; jt = headB
        if n1 > n2:
            for _ in range(n1 - n2):
                it = it.next
        if n2 > n1:
            for _ in range(n2 - n1):
                jt = jt.next
        while id(it) != id(jt):
            it = it.next; jt = jt.next
        return it