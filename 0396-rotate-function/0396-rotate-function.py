class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        n = len(nums)
        current_f = sum(i*num for i, num in enumerate(nums))
        max_f = current_f
        for k in range(1, n):
            current_f = current_f + total_sum - (n*nums[n-k])
            max_f = max(max_f, current_f)
        return max_f
        


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna