# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None
        copied_head = RandomListNode(head.label)
        get_copied_node = dict()
        get_copied_node[id(head)] = copied_head
        pre = copied_head
        it = head.next
        while it:
            copied_node = RandomListNode(it.label)
            pre.next = copied_node
            get_copied_node[id(it)] = copied_node
            pre = pre.next
            it = it.next
        it = head
        while it:
            if it.random == None:
                pass
            else:
                get_copied_node[id(it)].random = get_copied_node[id(it.random)]
            it = it.next
        return copied_head
            
        
        
