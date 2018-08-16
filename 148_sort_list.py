# Definition for singly-linked list.
from link_list import ListNode

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        heads = list()
        it = head
        while it:
            heads.append(it)
            tmp = it
            it = it.next
            tmp.next = None
        while len(heads) > 1:
            i, j = 0, 1
            new_heads = list()
            while j < len(heads):
                new_head = self.merge_sort(heads[i], heads[j])
                new_heads.append(new_head)
                i += 2; j += 2
            if i < len(heads):
                new_heads.append(heads[i])
            heads = new_heads
        return heads[0]
    
    def merge_sort(self, head1, head2):
        print("{},{}".format(head1.val, head2.val))
        it = head1; jt = head2
        if it.val < jt.val:
            new_head = kt = it
            it = it.next
        else:
            new_head = kt = jt
            jt = jt.next
        while it and jt:
            if it.val < jt.val:
                kt.next = it
                it = it.next
                kt = kt.next
            else:
                kt.next = jt
                jt = jt.next
                kt = kt.next
        while it:
            kt.next = it
            it = it.next
            kt = kt.next
        while jt:
            kt.next = jt
            jt = jt.next
            kt = kt.next
        return new_head

head = ListNode.generate_link_list([4, 2, 1, 3])
Solution().sortList(head)