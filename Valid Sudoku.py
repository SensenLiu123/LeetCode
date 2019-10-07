class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m = len(board);
        if m == 0:
            return False;
        
        n = len(board[0]);
        if n == 0 or m != n:
            return False; 
        
        
        for i in range(m):
            if not self.checkRow(board, i):
                return False;
            
        for j in range(n):
            if not self.checkCol(board, j):
                return False;
            
            
        for kr in range(m // 3):
            for kc in range(n // 3):
                if not self.checkPar(board, kr, kc):
                    return False; 
            
        return True;
    
    
    def checkRow(self, board, i):
        visited = set();
        for string in board[i]:
            if string == '.':
                continue;
            if string in visited:
                return False;
            visited.add(string);
            
        return True;
    
    
    def checkCol(self, board, j):
        visited = set();
        for r in range(len(board)):
            if board[r][j] =='.':
                continue;
            if board[r][j] in visited:
                return False;
            visited.add(board[r][j])
        return True;
    
    
    def checkPar(self, board, kr, kc):
        visited = set();
        for r in range(3*kr, 3* kr + 3):
            for c in range(3*kc, 3* kc + 3):
                if board[r][c] =='.':
                    continue;
                if board[r][c] in visited:
                    return False;
                visited.add(board[r][c])
        return True;