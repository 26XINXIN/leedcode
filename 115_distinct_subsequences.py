class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        distinct = [0] * len(s)
        first = -1
        for i in range(len(s)):
            if s[i] == t[0]:
                distinct[i] = 1
                if first == -1:
                    first = i
        for j in range(1, len(t)):
            print(distinct)
            new_distinct = [0] * len(s)
            new_first = -1
            last = 0
            for i in range(0, len(s)):
                if s[i] == t[j]:
                    new_distinct[i] = sum(distinct[:i])
                    # if new_first == -1:
                    #     new_distinct[i] = sum(distinct[:i])
                    #     new_first = last = i
                    # else:
                    #     new_distinct[i] = new_distinct[last] + sum(distinct[last + 1: i])
                    #     last = i
            distinct = new_distinct
            first = new_first
        return sum(distinct)


Solution().numDistinct("rabbbit", "rabbit")