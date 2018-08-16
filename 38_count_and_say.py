class Node:
    def __init__(self, v):
        self.count = 0
        self.value = v
        self.next = None


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        
        if n == 1:
            return "1"

        string = self.countAndSay(n-1)
        linked_list = Node(-1)
        it = linked_list
        for s in string:
            if s != it.value:
                it.next = Node(s)
                it = it.next
                it.count += 1
            else:
                it.count += 1
        it = linked_list.next
        re = ""
        while it:
            re += str(it.count) + it.value
            it = it.next
        return re