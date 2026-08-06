class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        for i in range(len(nums)): 
            if i > 0 and nums[i] == nums[i -1]: 
                continue 
            nums[l] = nums[i]
            l += 1
        return l

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna