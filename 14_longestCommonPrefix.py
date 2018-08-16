class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if strs == []:
            return ""

        prefix = ""
        while self.not_empty(strs):
            first = list()
            for n in range(len(strs)):
                first.append(strs[n][0])
                strs[n] = strs[n][1:]
            if first.count(first[0]) == len(strs):
                prefix += first[0]
            else:
                break
        return prefix

    def not_empty(self, strs):
        for str in strs:
            if str == "":
                return False
        return True
