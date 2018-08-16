# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        first = head
        last = head
        pre_node = dict()
        while last.next:
            pre_node[id(last.next)] = last
            last = last.next
        while first != last and first.next != last:
            last.next = first.next
            first.next = last
            first = last.next
            last = pre_node[id(last)]
        last.next = None