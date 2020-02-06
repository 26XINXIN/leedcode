class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        idxs = dict()
        neighbors = dict()
        last_idx = None
        for i, c in enumerate(s):
            if c not in idxs:
                idxs[c] = i
                neighbors[i] = [last_idx, None]
                last_idx = i
            else:
                if neighbors[idxs[c]][1] and c > s[neighbors[idxs[c]][1]]:
                    pre = idxs.pop(c)
                    p, n = neighbors.pop(pre)
                    neighbors[p][1] = n
                    neighbors[n][0] = p
                    idxs[c] = i
                    neighbors[i] = [last_idx, None]
                    last_idx = i
        return ''.join(idxs.keys())