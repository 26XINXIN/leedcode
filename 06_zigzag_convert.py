class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        rows = list(range(numRows))
        rows += list(range(numRows - 2, 0, -1))
        cycle = len(rows)
        # print(rows)
        ans = list()
        for i in range(numRows):
            ans.append("")

        for i in range(len(s)):
            ans[rows[i % cycle]] += s[i]
        # print(ans)

        answer = ""
        for ss in ans:
            answer += ss
        return answer

Solution().convert("ABC", 2)
