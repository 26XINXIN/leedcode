from queue import Queue
class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], containedBoxes: List[List[int]], initialBoxes: List[int]) -> int:
        searched = set()
        opened = set(i for i, s in enumerate(status) if s == 1)
        reachable = set(initialBoxes)
        searching = set(initialBoxes)
        while searching:
            newBoxes = set()
            for box in searching:
                for b in containedBoxes[box]:
                    newBoxes.add(b)
            newOpened = set()
            for box in searching:
                for key in keys[box]:
                    if status[key] == 0:
                        status[key] = 1
                        newOpened.add(key)
            searched = searched.union(searching)
            reachable = reachable.union(newBoxes)
            opened = opened.union(newOpened)
            searching = (newBoxes & opened) | (newOpened & reachable)
        return sum(candies[i] for i in searched)
                