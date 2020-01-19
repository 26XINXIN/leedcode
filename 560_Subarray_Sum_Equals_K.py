class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = [0]
        cnt = {0: 1}
        n = 0
        for i in range(len(nums)):
            accu = sums[-1] + nums[i]
            sums.append(accu)
            n += cnt.get(accu-k, 0)
            cnt[accu] = cnt.get(accu, 0) + 1
        return n
