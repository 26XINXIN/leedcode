class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        i = 0
        num = ""
        while str[i] == " ":
            i ++
        if str[i] == "-" or str[i] == "+":
            num += str[i]
            i++
        while str[i].isdigit():
            num += str[i]

        ans = 0
        try:
            ans = int(num)
        except:
            return 0

        ans = ans if ans <= 2147483647 else 2147483647
        ans = ans if ans >= -2147483648 else -2147483648
        return ans
