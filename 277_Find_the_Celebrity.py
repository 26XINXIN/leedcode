# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

# knows(a, b) = 1 --> a is not
# knows(a, b) = 0 --> b is not

class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = list(range(n))
        while len(candidate) > 1:
            if knows(candidate[-1], candidate[-2]):
                candidate.pop(-1)
            else:
                candidate.pop(-2)
        if all(not knows(candidate[0], j) for j in range(n) if j != candidate[0]) and all(knows(j, candidate[0]) for j in range(n) if j != candidate[0]):
            return candidate[0]
        else:
            return -1