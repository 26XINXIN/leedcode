class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        solution = list()

        for i in range(len(candidates)):
            tmp_target = target - candidates[i]
            if tmp_target == 0:
                solution.append([candidates[i]])
            elif tmp_target > 0:
                sub_solution = self.combinationSum(candidates[i:], tmp_target)
                for s in sub_solution:
                    s.append(candidates[i])
                    solution.append(s)
            else:
                pass
        return solution