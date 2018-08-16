class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n or head == None or head.next == None:
            return head
        
        header = ListNode(-1)
        header.next = head
        begin, prefix = head, header
        for _ in range(m-1):
            begin = begin.next
            prefix = prefix.next
        
        end = header
        for _ in range(n):
            end = end.next
        relink = end.next

        begin, end = self.reverse(begin, end)
        
        prefix.next = begin
        end.next = relink
        return header.next

    def reverse(self, begin, end):
        it, pre = begin.next, begin
        while it != end:
            tmp1, tmp2 = it.next, it
            it.next = pre
            it, pre = tmp1, tmp2
        it.next = pre
        return end, begin

def generate_link_list(l):
    header = ListNode(-1)
    it = header
    for e in l:
        it.next = ListNode(e)
        it = it.next
    return header.next

def print_link_list(head):
    l = list()
    it = head
    while it:
        l.append(it.val)
        it = it.next
    print(l)

l = [1, 2, 3, 4, 5]
head = generate_link_list(l)
Solution().reverseBetween(head, 2, 4)
print_link_list(head)