from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bull = 0
        scount = Counter()
        gcount = Counter()
        for s, g in zip(secret, guess):
            if s == g:
                bull += 1
            else:
                scount[s] = scount.get(s, 0) + 1
                gcount[g] = gcount.get(g, 0) + 1 
        cow = sum((scount & gcount).values())
        return '{}A{}B'.format(bull, cow)