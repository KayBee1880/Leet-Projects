class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefix_set = set()
        for num in arr1: 
            while num >0: 
                prefix_set.add(num)
                num //=10
        longest = 0
        for num in arr2: 
            while num > 0: 
                if num in prefix_set: 
                    current_length = len(str(num))
                    longest = max(longest, current_length)
                    break 
                num//=10
        return longest

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna