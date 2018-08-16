class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        zhengshu = ""
        if numerator * denominator < 0:
            zhengshu = "-"
        numerator = abs(numerator)
        denominator = abs(denominator)
        if numerator > denominator:
            zhengshu += str(numerator // denominator)
            numerator = numerator % denominator
        else:
            zhengshu += "0"
        
        xiaoshu = list()
        numerator *= 10
        weishu = [numerator]
        while numerator != 0:
            d = numerator // denominator
            numerator %= denominator
            xiaoshu.append(str(d))
            numerator *= 10
            if numerator in weishu:
                break
            else:
                weishu.append(numerator)
        if numerator == 0:
            result = zhengshu + "." + ''.join(xiaoshu)
        else:
            i = weishu.index(numerator)
            xiaoshu.insert(i, "(")
            xiaoshu.append(")")
            result = zhengshu + "." + "".join(xiaoshu)
        return result.strip(".")
        
        