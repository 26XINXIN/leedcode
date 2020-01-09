class Codec:
    def encode(self, strs: [str]) -> str:
        """Encodes a list of strings to a single string.
        """
        lengths = [len(s) for s in strs]
        nstrs = len(strs)
        encoded = str(nstrs) + '|' + '|'.join([str(l) for l in lengths]) + '|'
        encoded += ''.join(strs)
        return encoded

    def decode(self, s: str) -> [str]:
        """Decodes a single string to a list of strings.
        """
        i, j = 0, 0
        while s[j] != '|':
            j += 1
        nstrs = int(s[i:j])
        i = j + 1
        j += 1
        lengths = list()
        for _ in range(nstrs):
            while s[j] != '|':
                j += 1
            lengths.append(int(s[i:j]))
            j += 1
            i = j
        strs = list()
        for l in lengths:
            strs.append(s[i:i+l])
            i = i+l
        return strs
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))