# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = []
        self.current = nestedList
        self.index = -1
        self.treewalk()
    
    def next(self) -> int:
        cur, idx = self.current, self.index
        self.treewalk()
        return cur[idx].getInteger()

    def treewalk(self):
        self.index += 1
        while self.hasNext():
            print(self.listify(self.current), self.index)
            if self.index == len(self.current):
                self.current, self.index = self.stack.pop()
            elif self.current[self.index].isInteger():
                break
            else:
                self.stack.append((self.current, self.index + 1))
                self.current = self.current[self.index].getList()
                self.index = 0
                
    
    def hasNext(self) -> bool:
        return len(self.stack) > 0 or self.index < len(self.current)
    
    def listify(self, l):
        r = list()
        for i in l:
            if i.isInteger():
                r.append(i.getInteger())
            else:
                r.append(self.listify(i.getList()))
        return r

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())