class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if len(wordDict) == 0:
            return []
        word_set = set(wordDict)
        min_len = min([len(word) for word in word_set])
        max_len = max([len(word) for word in word_set])
        
        dp = []
        for i in range(len(s)):
            dp.append(list())
        i = 0
        while i < len(s):
            for j in range(min_len, max_len + 1):
                if i + j <= len(s) and s[i:i+j] in word_set:
                    dp[i + j - 1].append(i)

            j = 0
            while i + j < len(s) and j <= max_len and dp[i + j] == False:
                j += 1
            if j == max_len + 1:
                return []
            i = i + j + 1
            
        result = self.get_step("", s, dp, len(s)-1)
        return result
    
    def get_step(self, following, s, dp, i):
        result = list()
        for j in dp[i]:
            if j == 0:
                if i == len(s) - 1:
                    result.append(s[:i+1])
                else:
                    result.append(s[:i+1] + " " + following)
            else:
                if i == len(s) - 1:
                    new_following = s[j:i+1]
                else:
                    new_following = s[j:i+1] + " " + following
                result += self.get_step(new_following, s, dp, j-1)
        return result


    