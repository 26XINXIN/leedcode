class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        pre_sums = [0]
        S = 0
        cnt = 0
        for i in range(len(nums)):
            S += nums[i]
            S_lower = S - upper
            S_upper = S - lower
            l = self.binary_leftmost_search(pre_sums, S_lower)
            r = self.binary_rightmost_search(pre_sums, S_upper)
            cnt += l - r + 1
            self.binary_insert(pre_sums, S)

    
    def binary_insert(self, l, e):
        i = self.binary_rightmost_search(l, e)
        l.insert(i, e)
        
    def binary_leftmost_search(self, l, e):
        mid = len(l) // 2
        if len(l) == 1:
            return 0
        elif l[mid] >= e:
            i = self.binary_leftmost_search(l[: mid + 1], e)
        else:  # l[mid] < e:
            i = self.binary_leftmost_search(l[mid + 1 :], e) + mid + 1
        return i
            
    
    def binary_rightmost_search(self, l, e):
        mid = len(l) // 2
        if len(l) == 1:
            return 0
        elif l[mid] <= e:
            i = self.binary_rightmost_search(l[mid:], e) + mid
        else:  # l[mid] > e:
            i = self.binary_leftmost_search(l[:mid], e)
        return i