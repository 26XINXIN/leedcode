class Solution:
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        prob = {(r, c): 1}
        for _ in range(K):
            step = dict()
            # print(prob)
            for (x, y), p in prob.items():
                if 0 <= x + 1 < N and 0 <= y + 2 < N: step[(x+1, y+2)] = step.get((x+1, y+2), 0) + 0.125 * p
                if 0 <= x + 1 < N and 0 <= y - 2 < N: step[(x+1, y-2)] = step.get((x+1, y-2), 0) + 0.125 * p
                if 0 <= x - 1 < N and 0 <= y + 2 < N: step[(x-1, y+2)] = step.get((x-1, y+2), 0) + 0.125 * p
                if 0 <= x - 1 < N and 0 <= y - 2 < N: step[(x-1, y-2)] = step.get((x-1, y-2), 0) + 0.125 * p
                if 0 <= x + 2 < N and 0 <= y + 1 < N: step[(x+2, y+1)] = step.get((x+2, y+1), 0) + 0.125 * p
                if 0 <= x + 2 < N and 0 <= y - 1 < N: step[(x+2, y-1)] = step.get((x+2, y-1), 0) + 0.125 * p
                if 0 <= x - 2 < N and 0 <= y - 1 < N: step[(x-2, y-1)] = step.get((x-2, y-1), 0) + 0.125 * p
                if 0 <= x - 2 < N and 0 <= y + 1 < N: step[(x-2, y+1)] = step.get((x-2, y+1), 0) + 0.125 * p
            prob = step
        return sum(prob.values())