class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        if len(s) == 0 or s[0] == "0":
            return 0
        
        F = [0] * (len(s) + 1)
        F[0] = F[1] = 1
        for k in range(2, len(s) + 1):
            F[k] = F[k-1] + F[k-2]
        
        i = 0
        num = 1
        while i < len(s):
            if s[i] in "12":
                l = 0
                last = None
                while i < len(s) and s[i] in "12":
                    last = s[i]; l += 1; i += 1
                if i < len(s):
                    if last == "1" and s[i] != "0":
                        l += 1; i += 1
                    elif last == "2" and s[i] in "3456":
                        l += 1; i += 1
                    elif s[i] == "0":
                        i += 1; l -= 1
            elif s[i] == "0":
                return 0
            else:
                l = 1; i += 1
            num *= F[l]
        return num
            
            
                