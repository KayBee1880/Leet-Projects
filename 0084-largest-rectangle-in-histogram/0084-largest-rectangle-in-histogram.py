class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0
        for i, curr_height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > curr_height: 
                index, height = stack.pop()
                width = i - index
                area = width * height 
                max_area = max(area, max_area)
                start = index
            stack.append((start, curr_height))
        
        n = len(heights)
        while stack:
            index, height = stack.pop()
            width = n - index
            area = height * width
            max_area = max(area, max_area)
        return max_area
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna