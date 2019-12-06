class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        if lower == upper:
            if len(nums) == 0:
                return [str(lower)]
            else:
                return []
        if len(nums) == 0:
            return ["{}->{}".format(lower, upper)]
        ranges = list()
        
        if lower == nums[0]:
            pass
        elif lower + 1 == nums[0]:
            ranges.append(str(lower))
        else:
            ranges.append("{}->{}".format(lower, nums[0]-1))
        
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                pass
            elif nums[i] + 1 == nums[i+1]:
                pass
            elif nums[i] + 2 == nums[i+1]:
                ranges.append(str(nums[i] + 1))
            else:
                ranges.append("{}->{}".format(nums[i] + 1, nums[i + 1] - 1))

        if upper == nums[-1]:
            pass
        elif upper - 1 == nums[-1]:
            ranges.append(str(upper))
        else:
            ranges.append("{}->{}".format(nums[-1]+1, upper))

        return ranges