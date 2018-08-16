class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits = digits[::-1]
        carry = 0
        result = list()
        for i in range(len(digits)):
            if i == 0:
                carry, summ = self.one_bit_adder(digits[i], 1)
            else:
                carry, summ = self.one_bit_adder(digits[i], carry)
            result.append(summ)
        if carry == 1:
            result.append(carry)
        return result[::-1]
        
    def one_bit_adder(self, a, b):
        c = a + b
        return c // 10, c % 10
        