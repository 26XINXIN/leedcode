class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = ""
        i = len(a)-1; j = len(b) - 1
        carry = 0
        while i >= 0 and j >= 0:
            next_carry, summ = self.half_adder(int(a[i]), int(b[j]))
            carry, summ = self.half_adder(summ, carry)
            _, carry = self.half_adder(next_carry, carry)
            i -= 1; j -= 1
            result = str(summ) + result
        
        while i >= 0:
            carry, summ = self.half_adder(int(a[i]), carry)
            i -= 1
            result = str(summ) + result
        
        while j >= 0:
            carry, summ = self.half_adder(int(b[j]), carry)
            j -= 1
            result = str(summ) + result
        
        if carry == 1:
            result = "1" + result
        
        return result
            
    def half_adder(self, a, b):
        return int(bool(a) & bool(b)), int(bool(a) ^ bool(b))

Solution().addBinary("11", "1")