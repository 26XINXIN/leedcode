class Solution:
    def canCross(self, stones: List[int]) -> bool:
        dp = {0: set([0])}
        stone_idx = {loc: i for i, loc in enumerate(stones)}
        for i in range(len(stones)):
            if i not in dp: continue
            for prev_step in dp[i]:
                for step in [prev_step - 1, prev_step, prev_step + 1]:
                    if step <= 0: continue
                    next_stone = stones[i] + step
                    if next_stone in stone_idx:
                        if stone_idx[next_stone] in dp:
                            dp[stone_idx[next_stone]].add(step)
                        else:
                            dp[stone_idx[next_stone]] = set([step])
        
        return stone_idx[stones[-1]] in dp