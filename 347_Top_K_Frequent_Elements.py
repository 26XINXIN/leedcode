import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = dict()
        for n in nums:
            cnt[n] = cnt.get(n, 0) + 1
        
        heap = list()
        for n, c in cnt.items():
            if len(heap) < k:
                heapq.heappush(heap, (c, n))
            else:
                if c > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (c, n))
        
        return [x[1] for x in heap]
                