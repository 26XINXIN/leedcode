class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        s = str(x)

        if s[0] == "-":
            digits = s[1:]
            digits = digits[::-1]
            while digits[0] == "0" and len(digits) > 1:
                digits = digits[1:]
            answer = int("-" + digits)
            return answer if answer >= -2147483648 else 0
        else:
            s = s[::-1]
            while s[0] == "0" and len(s) > 1:
                s = s[1:]
            answer = int(s)
            return answer if answer <= 2147483647 else 0
