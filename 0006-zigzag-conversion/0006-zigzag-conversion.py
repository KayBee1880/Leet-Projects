class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows: 
            return s
        direction = 1 
        rows = [""]*numRows 
        curr_row = 0
        for char in s: 
            rows[curr_row] += char
            if curr_row == 0: 
                direction = 1
            elif curr_row == numRows - 1: 
                direction = -1 
            curr_row += direction 
        return "".join(rows)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna