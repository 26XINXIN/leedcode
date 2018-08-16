try:
    from queue import PriorityQueue
except:
    from Queue import PriorityQueue

class LRUCache:

    class ListNode:
        def __init__(self, key, value):
            self.key = key
            self.value = value
            self.next = None
            self.pre = None

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.items = dict()
        self.least_used_key = None
        self.lru = None
        self.last = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.items:
            it = self.items[key]
            self.move_to_last(it)
            result = it.value
        else:
            result = -1

        print("get {}".format(key))
        self.print_stat()
        return result
            
    def move_to_last(self, it):
        pre = it.pre
        nxt = it.next
        if not nxt:
            pass
        elif not pre:
            self.lru = nxt
            self.lru.pre = None
            self.last.next = it
            it.pre = self.last
            it.next = None
            self.last = it
        else:
            pre.next = nxt
            nxt.pre = pre
            it.pre = self.last
            self.last.next = it
            it.next = None
            self.last = it
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.items:
            self.items[key].value = value
            self.move_to_last(self.items[key])
        else:
            if len(self.items) == self.capacity:
                self.items.pop(self.lru.key)
                self.lru = self.lru.next
                if self.lru:
                    self.lru.pre = None
            if self.lru == None:
                self.lru = self.ListNode(key, value)
                self.last = self.lru
            else:
                node = self.ListNode(key, value)
                self.last.next = node
                node.pre = self.last
                self.last = self.last.next
            self.items[key] = self.last
        
        print("put {} {}".format(key, value))
        self.print_stat()

    def print_stat(self):
        it = self.lru
        while it:
            print("{}-".format(it.key),end="")
            it = it.next
        print("")
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)