from heapq import heappush, heappop

class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        scores = dict()
        for sid, score in items:
            if sid not in scores:
                scores[sid] = [-score]
            else:
                heappush(scores[sid], -score)
        
        print(scores)
        lscores = list()
        for sid, score in scores.items():
            avg = 0
            for _ in range(5):
                avg += -heappop(score)
            avg = int(avg / 5)
            lscores.append([sid, avg])
        lscores.sort()
        return lscores