class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()
        def dfs(r, c, index): 
            if index == len(word): 
                return True 
            if (r < 0 or r >= rows or 
            c < 0 or c >= cols or (r,c) in visited or word[index] != board[r][c]): return False 
            visited.add((r,c))
            found = (dfs(r+1, c, index +1) or dfs(r-1, c, index + 1) or dfs(r, c+1, index + 1) or dfs(r, c-1, index +1))
            visited.remove((r,c))
            return found 
        for r in range(rows): 
            for c in range(cols): 
                if dfs(r,c, 0): 
                    return True 
        return False 

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna