class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Monotonic decreasing stack helps to find the greater temperature and location well 
        stack = []
        n = len(temperatures)
        answer = [0] * n
        for curr_day, curr_temp in enumerate(temperatures): 
            while stack and temperatures[stack[-1]] < curr_temp: 
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day
            stack.append(curr_day)
        return answer

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna