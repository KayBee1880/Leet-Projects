class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = Counter(nums)
        max_count = 0
        majority = nums[0]
        for key, val in count.items(): 
            if val > max_count:
                max_count = val 
                majority = key
        return majority

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna