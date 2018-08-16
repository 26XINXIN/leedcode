class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        directions = path.split("/")
        stack = list()
        for d in directions:
            if d == "." or d == "":
                continue
            elif d == "..":
                if len(stack) == 0 or stack[-1] == "..":
                    stack.append("..")
                else:
                    stack.pop()
            else:
                stack.append(d)

        path = ""
        for p in stack:
            path += "/" + p
        if path == "":
            path = "/"
        return path