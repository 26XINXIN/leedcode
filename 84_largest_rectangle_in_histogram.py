class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        widths = [0, len(heights)]
        maximum_area = 0
        while len(widths) > 0:
            new_widths = list()
            for left, right in widths:
                max_height = min(heights[left, right])
                maximum_area = max(max_height, max_height * (left - right))
                try:
                    while 1:
                        idx = heights.index(max_height, left, right)
                        new_widths.append((left, idx))
                        left = idx + 1
                except:
                    new_widths.append((left, right))
        return maximum_area

                
                    
