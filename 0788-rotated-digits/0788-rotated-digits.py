class Solution:
    def rotatedDigits(self, n: int) -> int:
        invalid_digits = {"3", "4", "7"}
        changing_digits = {"2","5", "6", "9"}
        good_count = 0
        for i in range(1, n+1):
            num = str(i)
            if any(d in invalid_digits for d in num):
                continue
            if any(d in changing_digits for d in num): 
                good_count += 1
        return good_count 

    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/leethub-v4/bcilpkkbokcopmabingnndookdogmbna