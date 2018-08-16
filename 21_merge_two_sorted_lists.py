# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        new_list = ListNode(-1)
        ptr = new_list
        while l1 != None and l2!= None:
            if l1.val < l2.val:
                ptr.next = ListNode(l1.val)
                l1 = l1.next
            else:
                ptr.next = ListNode(l2.val)
                l2 = l2.next
            ptr = ptr.next
        while l1 != None:
            ptr.next = ListNode(l1.val)
            l1 = l1.next; ptr = ptr.next
        while l2 != None:
            ptr.next = ListNode(l2.val)
            l2 = l2.next; ptr = ptr.next
        return new_list.next