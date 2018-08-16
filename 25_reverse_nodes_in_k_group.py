# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        first, last = head, head
        
        while last != None:
            tmp_list = list()
            for _ in range(k):
                if last == None:
                    break
                else:
                    tmp_list.append(last)
                    last = last.next

