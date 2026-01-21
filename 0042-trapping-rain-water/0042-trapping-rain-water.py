class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        total_water = 0
        for i in range(1,len(height)-1): 
            left_max = max(height[:i])
            right_max = max(height[i+1:]) 
            total_water += max(0, min(left_max, right_max) - height[i])
        return total_water