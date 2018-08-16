class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        str_num = str(x)
        if str_num[0] == "-":
            return False
        re_num = str_num[::-1]
        if str_num == re_num:
            return True
        else:
            return False
