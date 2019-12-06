from itertools import product
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        sbg = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
        }
        
        if n == 0:
            return []
        if n == 1:
            return ['0', '1', '8']
        
        result = product(['1', '6', '8', '9'], product(sbg.keys(), repeat=n//2 - 1))
        result = [r[0] + ''.join(r[1]) for r in result]
        if n % 2 == 1:
            result = [r + c for r, c in product(result, ['0', '1', '8'])]
        for i in range(len(result)):
            for j in range(n // 2 - 1, -1, -1):
                result[i] += sbg[result[i][j]]
        return result
        
