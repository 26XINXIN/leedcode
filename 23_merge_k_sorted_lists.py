# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from Queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        q = PriorityQueue()

        if not self.valid(lists):
            return None

        for i in range(len(lists)):
            if lists[i] != None:
                q.put((lists[i].val, i))

        ans = ListNode(-1)
        ptr = ans
        while not q.empty():
            val, i = q.get()
            ptr.next = ListNode(val)
            lists[i] = lists[i].next
            ptr = ptr.next
            if lists[i] != None:
                q.put((lists[i].val, i))
        return ans.next

    def valid(self, lists):
        empty_lists = True
        for i in range(len(lists)):
            if lists[i] != None:
                empty_lists = False
        if (len(lists) == 0
            or empty_lists):
            return False
        else:
            return True
