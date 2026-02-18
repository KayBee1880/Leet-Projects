class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        def count_live_neighbours(r, c):
            direction = [(-1,-1), (-1,0), (-1,1),
            (0,-1),(0,1),
            (1,-1),(1,0),(1,1)]
            live_neighbours = 0
            for dr, dc in direction:
                nr, nc = r+dr, c + dc
                if 0<=nr<m and 0<=nc<n and abs(board[nr][nc])==1:
                    live_neighbours += 1
            return live_neighbours
        # first pass (assigning temporal states)
        for i in range(m):
            for j in range(n):
                live_neighbours = count_live_neighbours(i, j)
                if board[i][j] == 1 and (live_neighbours < 2 or live_neighbours > 3):
                    board[i][j] = -1
                if board[i][j] == 0 and live_neighbours == 3:
                    board[i][j] = 2
        #2nd pass 
        for i in range(m): 
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1