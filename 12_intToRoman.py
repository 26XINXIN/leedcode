class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        thousands = num // 1000
        num %= 1000
        hundreds = num // 100
        num %= 100
        tens = num // 10
        ones = num % 10

        hundred = {
            0: "",
            1: "C",
            2: "CC",
            3: "CCC",
            4: "CD",
            5: "D",
            6: "DC",
            7: "DCC",
            8: "DCCC",
            9: "CM",
        }

        ten = {
            0: "",
            1: "X",
            2: "XX",
            3: "XXX",
            4: "XL",
            5: "L",
            6: "LX",
            7: "LXX",
            8: "LXXX",
            9: "XC",
        }

        one = {
            0: "",
            1: "I",
            2: "II",
            3: "III",
            4: "IV",
            5: "V",
            6: "VI",
            7: "VII",
            8: "VIII",
            9: "IX",
        }

        roman = ""
        roman += "M" * thousands
        roman += hundred[hundreds]
        roman += ten[tens]
        roman += one[ones]

        return roman
