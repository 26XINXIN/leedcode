class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        low, low2 = None, None
        for n in nums:
            if low is None or n < low:
                low = n
            elif low2 is None or n < low2:
                low2 = n
            else:
                return True
        return False