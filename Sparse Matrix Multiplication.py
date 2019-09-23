class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        # assume A cols == B rows 
        m, p, n = len(A), len(A[0]), len(B[0])
        C = [[0] * n for i in range(m)]
        
        
        nonZeroA = []
        nonZeroB = []
        
        for r in range(m):
            nonZeroA.append(set())
            for c in range(p):
                if A[r][c] == 0:
                    continue 
                    
                nonZeroA[r].add(c)
                
        for c in range(n):
            nonZeroB.append(set())
            for r in range(p):
                if B[r][c] == 0:
                    continue 
                    
                nonZeroB[c].add(r)
                
                
                
        for i in range(m):
            for j in range(n):
                for k in nonZeroA[i] & nonZeroB[j]:
                    C[i][j] += A[i][k] * B[k][j]
                    
        return C
                