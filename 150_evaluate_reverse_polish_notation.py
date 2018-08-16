from math import trunc

class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = list()
        for t in tokens:
            try:
                stack.append(int(t))
                continue
            except:
                pass
            if t == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif t == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif t == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            elif t == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(trunc(b / a))
        return stack.pop()
        
