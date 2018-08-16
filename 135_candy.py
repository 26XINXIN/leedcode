class Solution(object):
    def __init__(self):
        self.ratings = None
        self.assignment = None
    
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n = len(ratings)
        if n == 0: return 0
        elif n == 1: return 1
        
        self.ratings = ratings
        self.assignment = [0] * n
        for i in range(n):
            if self.assignment[i] == 0:
                self.candy_of(i)
        return sum(self.assignment)
    
    def candy_of(self, i):
        if i == 0:
            if self.ratings[i] > self.ratings[i + 1]:
                if self.assignment[i + 1] == 0:
                    right = self.candy_of(i + 1)
                else:
                    right = self.assignment[i + 1]
                self.assignment[i] = right + 1
            else:
                self.assignment[i] = 1
        elif i == len(self.ratings) - 1:
            if self.ratings[i] > self.ratings[i-1]:
                if self.assignment[i-1] == 0:
                    left = self.candy_of(i-1)
                else:
                    left = self.assignment[i-1]
                self.assignment[i] = left + 1
            else:
                self.assignment[i] = 1
        else:
            left = right = 0
            if self.ratings[i] > self.ratings[i + 1]:
                if self.assignment[i + 1] == 0:
                    right = self.candy_of(i + 1)
                else:
                    right = self.assignment[i + 1]
            if self.ratings[i] > self.ratings[i-1]:
                if self.assignment[i-1] == 0:
                    left = self.candy_of(i-1)
                else:
                    left = self.assignment[i-1]
            self.assignment[i] = max(left, right) + 1
        return self.assignment[i]

ratings = [1, 0, 2]
print(Solution().candy(ratings))