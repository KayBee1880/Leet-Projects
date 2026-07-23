from functools import lru_cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache
        def match(i, j): 
            if j == len(p): 
                return i == len(s)
            first_match = (i < len(s) and (s[i] == p[j] or p[j] == "."))
            if j + 1 < len(p) and p[j+1] == "*": 
                return (match(i, j+2) or 
                (first_match and match(i+1, j)))
            return first_match and match(i+1,j+1)
        return match(0,0)

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna