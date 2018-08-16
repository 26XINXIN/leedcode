# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        l = ListNode(-1)
        new_head = l
        tail = head
        current = head
        for i in range(n):
            tail = tail.next
        while tail != None:
            l.next = ListNode(current.val)
            l = l.next
            tail = tail.next
            current = current.next
        current = current.next
        while current != None:
            l.next = ListNode(current.val)
            l = l.next; current = current.next
        return new_head.next

head = ListNode(1)
ptr = head
for i in range(2, 6):
    ptr.next = ListNode(i)
    ptr = ptr.next

res = Solution().removeNthFromEnd(head, 2)
l_res = list()
while res != None:
    l_res.append(res.val)
    res = res.next
print(l_res)
