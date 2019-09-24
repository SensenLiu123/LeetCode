import collections 
DIR = [(0,1), (0, -1), (1, 0), (-1, 0)]
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        if m == 0:
            return board
        n = len(board[0])
        if m <= 1 or n <= 1:
            return board
        for c in range(n):
            if board[0][c] == 'O':
                self.markIsland(board, 0 , c)
            if board[m - 1][c] == 'O':    
                self.markIsland(board, m -1, c)
            
            
        for r in range(m):
            if board[r][0] == 'O':
                self.markIsland(board, r, 0)
            if board[r][n - 1] == 'O':
                self.markIsland(board, r, n - 1)
            
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                    
                if board[i][j] == 'A':
                    board[i][j] = 'O'
                    
                else:
                    continue
                    
        return 
    
    def markIsland(self, board, x ,y):
        queue = collections.deque([(x, y)])
        
        while queue:
            x, y = queue.popleft()
            board[x][y] = 'A'
            for dx, dy in DIR:
                nx, ny = x + dx, y + dy
                if not self.valid(board, nx, ny):
                    continue 
                    
                if board[nx][ny] == 'O':
                    board[nx][ny] = 'A'
                    queue.append((nx, ny))
                    
    def valid(self, board, x, y):
        m, n = len(board), len(board[0])
        return 0 <= x < m and 0 <= y < n
                    
        
            
    
                    
                    
                    
            
        