class Solution:
    def isRectangleOverlap(self, rec1, rec2):
        """
        :type rec1: List[int]
        :type rec2: List[int]
        :rtype: bool
        """
        return self.overlap(rec1[::2], rec2[::2]) and self.overlap(rec1[1::2], rec2[1::2])

    def overlap(self, r1, r2):
        if r1[0] < r2[0]:
            if r2[0] < r1[1]:
                return True
            else:
                return False
        elif r1[0] == r2[0]:
            return True
        else:
            if r1[0] < r2[1]:
                return True
            else:
                return False