class Solution:
    def reverseParentheses(self, s: str) -> str:
        # begins = list()
        result = ''
        i = 0
        while i < len(s):
            if s[i] == '(':
                # begins.append(i)
                substring, j = self.reverse(s, i)
                result += substring
                i = j + 1
            else:
                result += s[i]
                i += 1
        return result
    
    def reverse(self, s, start):
        result = ''
        i = start + 1
        while i < len(s):
            if s[i] == '(':
                substring, j = self.reverse(s, i)
                result += substring
                i = j + 1
            elif s[i] == ')':
                return result[::-1], i
            else:
                result += s[i]
                i += 1
        return result[::-1], i
                
                

            
            
                

s = "a(bcdefghijkl(mno)p)q"
print(Solution().reverseParentheses(s))