class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        digits = dict()
        for i in range(4):
            digits[i] = ""
        i = 0
        flag = 0
        for i in range(len(s)):
            if flag == 0:
                if s[i] == "M":
                    digits[0] += s[i]
                else:
                    flag = 1
            if flag == 1:
                if s[i] in "CDM":
                    digits[1] += s[i]
                else:
                    flag = 2
            if flag == 2:
                if s[i] in "XLC":
                    digits[2] += s[i]
                else:
                    flag = 3
            if flag == 3:
                digits[3] += s[i]

        hundred = {
            "" : 0,
            "C": 1,
            "CC": 2,
            "CCC": 3,
            "CD": 4,
            "D": 5,
            "DC": 6,
            "DCC": 7,
            "DCCC": 8,
            "CM": 9,
        }

        ten = {
            "": 0,
            "X": 1,
            "XX": 2,
            "XXX": 3,
            "XL": 4,
            "L": 5,
            "LX": 6,
            "LXX": 7,
            "LXXX": 8,
            "XC": 9,
        }

        one = {
            "": 0,
            "I": 1,
            "II": 2,
            "III": 3,
            "IV": 4,
            "V": 5,
            "VI": 6,
            "VII": 7,
            "VIII": 8,
            "IX": 9,
        }

        num = len(digits[0]) * 1000 + hundred[digits[1]] * 100 + ten[digits[2]] * 10 + one[digits[3]]
        return num

Solution().romanToInt("DCXXI")
