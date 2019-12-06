class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        sbg = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
        }
        
        if len(num) == 0: return True

        for i in range((len(num)+ 1) // 2):
            if num[i] not in sbg or num[-i-1] != sbg[num[i]]:
                return False
        return True