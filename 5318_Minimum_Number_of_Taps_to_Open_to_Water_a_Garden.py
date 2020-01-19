class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        taps = sorted(enumerate(ranges), key=lambda x: x[0] - x[1])
        max_right = taps[0][0] + taps[0][1]
        i = 1
        while i < len(taps):
            if taps[i][0] - taps[i][1] > max_right:
                return -1
            if taps[i][0] + taps[i][1] <= max_right:
                taps.pop(i)
            else:
                max_right = max(max_right, taps[i][0] + taps[i][1])
                i+=1
        
        min_taps = self.search(0, taps, 0)
        return min_taps if min_taps <= 1e4+1 else -1
    
    def search(self, watered, taps, n):
        # print(watered, taps)
        if not taps:
            return 1e4 + 2
        min_taps = 1e4 + 2
        for k, (t, r) in enumerate(taps):
            if t + r >= len(watered):
                return n+1
            min_taps = min(min_taps, self.search(t + r - 1, filter(taps, lambda x: x[i] > t + r - 1), n+1))
        return min_taps