class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = list()

        for c in s:
            if c == "(":
                stack.append(c)
            else:
                if len(stack) > 0 and stack[-1] == "(":
                    stack.pop()
                    if len(stack) > 0 and isinstance(stack[-1], int):
                        stack[-1] += 1
                    else:
                        stack.append(1)
                elif len(stack) > 1 and stack[-1] != ")" and stack[-2] == "(":
                    tmp = stack[-1] + 1
                    stack.pop(); stack.pop()
                    if len(stack) > 0 and isinstance(stack[-1], int):
                        stack[-1] += tmp
                    else:
                        stack.append(tmp)
                else:
                    stack.append(c)
        print(stack)

        l = 0
        for ele in l:
            if isinstance(ele, int) and ele > l:
                l = ele
        return l

Solution().longestValidParentheses("()(())")