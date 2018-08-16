class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = self.generateNParen(n)
        return list(ans)

    def generateNParen(self, n):
        if n == 1:
            ans = {"()"}
            return ans
        else:
            ans = set()
            for i in range(1, n):
                left = self.generateNParen(i)
                right = self.generateNParen(n-i)
                for l in left:
                    for r in right:
                        ans.add(l+r)
            ans2 = self.generateNParen(n-1)
            for a in ans2:
                ans.add("(" + a + ")")
            return ans


