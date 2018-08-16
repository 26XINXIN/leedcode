class Solution:
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        return self.combinationSum(candidates, target)

    def combinationSum(self, candidates, target):
        
        solution = list()
        for i in range(len(candidates)):
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            tmp_target = target - candidates[i]
            if tmp_target == 0:
                solution.append([candidates[i]])
            elif tmp_target > 0:
                # j = i
                # while candidates[j] == candidates[i]:
                #     j += 1
                sub_solution = self.combinationSum(candidates[i+1:], tmp_target)
                for s in sub_solution:
                    s.append(candidates[i])
                    solution.append(s)
            else:
                pass
        return solution