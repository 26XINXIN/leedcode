class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = list()
        for c in s:
            if c in "([{":
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if (
                    (c == ")" and stack[-1] == "("),
                    or (c == "]" and stack[-1] == "[")
                    or (c == "}" and stack[-1] == "{")):
                    stack.pop()
                else:
                    return False
        if len(stack) == 0:
            return True
        else:
            return False
