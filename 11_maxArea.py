class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxa = 0
        sorted_height = list(height)
        sorted_height.sort()
        for h in sorted_height[::-1]:
            first = -1
            last = -1
            for i in range(len(height)):
                if height[i] >= h:
                    if first == -1:
                        first = i
                    last = i
            area = h * (last - first)
            maxa = (maxa if maxa > area else area)
            print("{},{},{},{}".format(first, last, area, maxa))
        return maxa

    def newMaxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        maxa = 0
        for i in range(len(height)):
            h = height[i]
            farest = len(height) - 1
            while height[farest] < h:
                farest -= 1
            area = h * (farest - i)
            maxa = (maxa if maxa > area else area)
        return maxa

height = [1,2,4,3]
print(Solution().maxArea(height))
