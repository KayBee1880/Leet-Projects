class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return 
        n = len(nums)
        k %= n 
        def _reverse(l, r): 
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l +=1
                r -= 1
        _reverse(0, n-1)
        _reverse(0, k-1)
        _reverse(k, n-1)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna