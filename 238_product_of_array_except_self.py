class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        left = [prod]
        for n in nums[:-1]:
            prod *= n
            left.append(prod)
        prod = 1
        right = [prod]
        for n in nums[::-1][:-1]:
            prod *= n
            right.append(prod)
        right = right[::-1]
        return [l * r  for l, r in zip(left, right)]
        
            