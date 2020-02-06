class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        if len(arr) == 0:
            return 0
        if len(arr) == 1:
            return 1
        visited = set([i for i in range(len(arr)) if (i == 0 and arr[i] > arr[i+1]) or (i == len(arr)-1  and arr[i] > arr[i-1]) or (0 < i < len(arr)-1 and (arr[i] > arr[i-1] or arr[i] > arr[i+1]))])
        if not visited:
            return 1
        # visited = set(range(len(arr)))
        steps = 0
        while visited:
            reachable = set()
            for i in visited:
                maxh = 0
                for step in range(1, d+1):
                    if i-step < 0 or maxh >= arr[i]:
                        break
                    if i-step in reachable:
                        continue
                    if arr[i] > arr[i-step] and arr[i] > maxh:
                        reachable.add(i - step)
                    maxh = max(maxh, arr[i-step])
                    # if maxh > arr[i]:
                    #     break
                maxh = 0
                for step in range(1, d+1):
                    if i+step >= len(arr) or maxh >= arr[i]:
                        break
                    if i+step in reachable:
                        continue
                    if arr[i] > arr[i+step] and arr[i] > maxh:
                        reachable.add(i + step)
                    maxh = max(maxh, arr[i+step])
                    # if maxh > arr[i]:
                    #     break
            visited = reachable
            steps += 1
        return steps
