class LargestNumKey(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """

        nums = sorted(map(str, nums), key=LargestNumKey)
        result = "".join(nums)
        return "0" if int(result) == 0 else result

