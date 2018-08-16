class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        b = bin(n)
        m = b[2:][::-1]
        zeros = "0" * (32 - len(m))
        m = m + zeros
        return int(m, base=2)