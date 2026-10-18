class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = strs[0]
        for i in range(1, len(strs)): 
            while not strs[i].startswith(prefix): 
                prefix = prefix[:-1]
        return prefix


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna