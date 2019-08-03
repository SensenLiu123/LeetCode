class Solution:
    
    def knightDialer(self, N: int) -> int:
        oneStep = [[4,6], [6,8], [7,9],[4,8],[0,9,3],[],[1,0,7], [2,6],[1,3],[4,2]]
        
        
        
        memo = {}
        totalHop = 0
        for position in range(10):
             
            totalHop += self.hopdfs(position, N, oneStep, memo)
            
        return totalHop  % (10 ** 9 + 7)
    
    def hopdfs(self, cur, remainHop, oneStep ,memo):
        
        if (cur, remainHop) in memo:
            return memo[(cur, remainHop)]
        
        if remainHop == 0:
            memo[(cur, 0)] = 1
            return 1
        
        if remainHop == 1:
            memo[(cur, 1)] = 1
            return 1
        
        steps = 0
        for neighbor in oneStep[cur]:
            steps += self.hopdfs(neighbor, remainHop -1 , oneStep, memo)
            
        memo[(cur, remainHop)] = steps %  (10 ** 9 + 7)
        return steps
        