class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        if not word:
            return []
        res = list()
        for c in word:
            new_res = list()
            for r in res:
                # insert not masking
                new_res.append(r + [c])
                # insert masked
                if isinstance(r[-1], int):
                    new_res.append(r[:-1] + [r[-1] + 1])
                else:
                    new_res.append(r + [1])
        return res
            
