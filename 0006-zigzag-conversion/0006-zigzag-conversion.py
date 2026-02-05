class Solution:
    def convert(self, s: str, numRows: int) -> str:
        #first solution O(n) time O(1) space because the res created is needed to display the final output hence not really counted as extra space
        #first approach 
      
        if numRows == 1 or numRows > len(s): return s
        rows = [""]*min(numRows, len(s))
        index, step = 0, 1
        for i in range(len(s)):
            rows[index] += s[i]
            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = - 1
            index += step
        return "".join(rows)

        