class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.map = {i: list() for i in range(10000)}

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        _key = key % 10000
        idx = 0 
        while idx < len(self.map[_key]) and self.map[_key][idx][0] != key:
            idx += 1
        if idx == len(self.map[_key]):
            self.map[_key].append((key, value))
        else:
            self.map[_key].pop(idx)
            self.map[_key].append((key, value))

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        _key = key % 10000
        for k, v in self.map[_key]:
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        _key = key % 10000
        idx = 0 
        while idx < len(self.map[_key]) and self.map[_key][idx][0] != key:
            idx += 1
        if idx != len(self.map[_key]):
            self.map[_key].pop(idx)
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)