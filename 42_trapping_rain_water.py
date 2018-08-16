class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) == 0:
            return 0
        area = 0

        left = 0; left_height = height[0]
        right = len(height) - 1; right_height = height[-1]
        while left != right:
            while left_height <= right_height and left != right:
                print("left:{},{},{},{}".format(left, right, left_height, right_height))
                area += left_height
                left += 1
                left_height = left_height if left_height > height[left] else height[left]
                
            while right_height < left_height and left != right:
                
                print("right:{},{},{},{}".format(left, right, left_height, right_height))
                area += right_height
                right -= 1
                right_height = right_height if right_height > height[right] else height[right]

        area += left_height
        return area - sum(height)


height = [0,1,0,2,1,0,1,3,2,1,2,1]
s = Solution()
print(s.trap(height))