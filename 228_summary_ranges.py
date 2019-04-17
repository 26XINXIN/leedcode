class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        left, right = nums[0], nums[0]
        ranges = list()
        i = 1
        while i < len(nums):
            if nums[i] == right + 1:
                right += 1
                i += 1
            else:
                if left == right:
                    ranges.append(str(left))
                else:
                    ranges.append('{}->{}'.format(left, right))
                    i += 1
                    left, right = nums[i], nums[i]
                    i += 1
        if left == right:
            ranges.append(str(left))
        else:
            ranges.append('{}->{}'.format(left, right))
        return ranges