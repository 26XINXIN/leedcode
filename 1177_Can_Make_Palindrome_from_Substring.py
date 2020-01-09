class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        prefix_cnt = [[0] * 26]
        for i in range(len(s)):
            cnt = list(prefix_cnt[-1])
            cnt[ord(s[i]) - ord('a')] += 1
            prefix_cnt.append(cnt)
        
        ans = list()
        for left, right, k in queries:
            cnt = [a - b for a, b in zip(prefix_cnt[right + 1], prefix_cnt[left])]
            need = sum(a % 2 for a in cnt) // 2
            ans.append(need <= k)
        
        return ans
            