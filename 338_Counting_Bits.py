class Solution:
    def countBits(self, num: int) -> List[int]:
        nbits = [0]
        while len(nbits) < num + 1:
            l = len(nbits)
            for i in range(l):
                nbits.append(nbits[i] + 1)
                if l + i == num:
                    break
        return nbits
                    
                