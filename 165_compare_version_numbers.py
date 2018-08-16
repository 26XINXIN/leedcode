class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))
        i = 0
        while i < min(len(v1), len(v2)):
            if v1[i] == v2[i]:
                i += 1
            elif v1[i] < v2[i]:
                return -1
            else:
                return 1
        if i == len(v1):
            while i < len(v2):
                if v2[i] > 0:
                    return -1
                i += 1
        if i == len(v2):
            while i < len(v1):
                if v1[i] > 0:
                    return 1
                i += 1
        return 0