class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        answer = str()
        pals = list()
        for i in range(len(s)):
            new_pals = list()
            for sub in pals:
                if i - len(sub) - 1 >= 0 and s[i - len(sub) - 1] == s[i]:
                    new_pals.append(s[i - len(sub) - 1] + sub + s[i])
            if i > 0 and s[i] == s[i-1]:
                new_pals.append(s[i-1:i+1])
            new_pals.append(s[i])
            pals = new_pals
            if len(answer) < len(new_pals[0]):
                answer = new_pals[0]

        return answer

answer = Solution().longestPalindrome("babaddtattarrattatddetartrateedredividerb")
print(answer)
