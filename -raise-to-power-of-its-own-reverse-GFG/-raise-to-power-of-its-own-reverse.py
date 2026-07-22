class Solution:
    def reverseExponentiation(self, n):
        # code here
        reversed_n = int(str(n)[::-1])
        def _exponent(n, power): 
            if power == 0: 
                return 1
            half = _exponent(n, power//2)
            if power % 2 == 0: 
                return half * half
            return n * half * half
        return _exponent(n, reversed_n)
        
            

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna