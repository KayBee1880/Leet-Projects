class Solution:
    def totalNQueens(self, n: int) -> int:
        result = []
        board = [["."]*n for i in range(n)]
        antidiag_set = set()
        diag_set = set()
        col_set = set()
        def backtrack(row): 
            if row == n: 
                result.append(["".join(line) for line in board])
                return 
            for col in range(n): 
                diag = row - col 
                antidiag = row + col 
                if col in col_set or diag in diag_set or antidiag in antidiag_set: 
                    continue 
                col_set.add(col)
                antidiag_set.add(antidiag)
                diag_set.add(diag)
                board[row][col] = "Q"
                backtrack(row + 1)
                col_set.remove(col)
                antidiag_set.remove(antidiag)
                diag_set.remove(diag)
                board[row][col] = "."
        backtrack(0)
        return len(result) 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna