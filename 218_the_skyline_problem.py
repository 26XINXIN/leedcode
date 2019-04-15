from typing import List
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        if not buildings:
            return []
        lefts = sorted([[idx, b[0], b[2]] for idx, b in enumerate(buildings)], key=lambda x: (x[1], -x[2]))
        rights = sorted([[idx, b[1], b[2]] for idx, b in enumerate(buildings)], key=lambda x: (x[1], x[2]))
        
        skyline = list()
        left_idx = 1
        right_idx = 0

        num_buildings = len(buildings)
        skyline.append([lefts[0][1], lefts[0][2]])
        heights = {lefts[0][0]: lefts[0][2]}
        while left_idx < num_buildings and right_idx < num_buildings:
            if lefts[left_idx][1] > rights[right_idx][1]:
                idx, loc, h = rights[right_idx]
                heights.pop(idx)
                hs = list(heights.values())
                # print(hs)
                h = max(hs) if hs else 0
                if h < skyline[-1][1]:
                    skyline.append([loc, h])
                right_idx += 1
            else:
                idx, loc, h = lefts[left_idx]
                heights[idx] = h
                if h > skyline[-1][1]:
                    skyline.append([loc, h])
                left_idx += 1
            
        while right_idx < num_buildings:
            idx, loc, h = rights[right_idx]
            heights.pop(idx)
            hs = list(heights.values())
            h = max(hs) if hs else 0
            if h < skyline[-1][1]:
                skyline.append([loc, h])
            right_idx += 1
        return skyline

buildings = [[1,2,1],[1,2,2],[1,2,3]]
print(Solution().getSkyline(buildings))