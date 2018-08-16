class Solution:
    def __init__(self):
        self.table = [
            " ", "?", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
        ]

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        res = list()
        for d in digits:
            d = int(d)
            if len(res) == 0:
                for c in self.table[d]:
                    res.append(c)
                continue
            new_res = list()
            for c in self.table[d]:
                for string in res:
                    new_res.append(string + c)
            res = new_res
        return res