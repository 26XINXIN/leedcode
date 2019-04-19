from typing import List
class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        arith_seq = list() # start, step, length
        diff = max(A) - min(A)
        max_len = 1
        for i in range(len(A)-1, -1, -1):
            new_arith_seq = list()
            new_arith_seq.append([i, 0, 1])
            for start, step, length in arith_seq:
                if length == 1:
                    if len(A) - start >= max_len:
                        new_arith_seq.append([start, step, length])
                    new_step = A[start] - A[i] 
                    if new_step * max_len <= diff:
                        new_arith_seq.append([i, new_step, length + 1])
                elif A[start] - A[i] == step:
                    new_arith_seq.append([i, step, length + 1])
                else:
                    new_arith_seq.append([start, step, length])
            arith_seq = new_arith_seq
            max_len = max(l for _, _, l in arith_seq)
            print(i, A[i], arith_seq)
        return max_len
            

A = [24,13,1,100,0,94,3,0,3]
print(Solution().longestArithSeqLength(A))