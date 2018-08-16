class Solution:
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        bm = bin(m)[2:]
        bn = bin(n)[2:]
        bm = '0' * (32-len(bm)) + bm
        bn = '0' * (32-len(bn)) + bn
        r = ''
        for i in range(32):
            if bm[i] == '1' and bn[i] == '1':
                r += '1'
            else:
                r += '0'
        return int(r, base=2)