# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        header = ListNode(-1)
        header.next = head
        insert = header
        it, pre = head, header
        while it:
            print(it.val)
            if it.val < x:
                if insert == pre:
                    insert = insert.next
                    it = it.next
                    pre = pre.next
                else:
                    next_ins = insert.next
                    insert.next = it
                    pre.next = it.next
                    it.next = next_ins
                    insert = insert.next
                    it = pre.next
            else:
                it = it.next
                pre = pre.next
        return header.next

def generate_list(l):
    head = ListNode(-1)
    it = head
    for n in l:
        it.next = ListNode(n)
        it = it.next
    return head.next

def print_list(head):
    l = list()
    it = head
    while it:
        print(it.val, end=",")
        l.append(it.val)
        it = it.next
    print(l)

head = generate_list([1,4,3,2,5,2])
head = Solution().partition(head, 3)
print_list(head)