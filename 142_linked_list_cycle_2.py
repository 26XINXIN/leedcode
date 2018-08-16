# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        nodes_id = [id(head)]
        it = head.next
        while it != None and id(it) not in nodes_id:
            nodes_id.append(id(it))
            it = it.next
        if it == None:
            return None
        else:
            return it