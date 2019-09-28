class Solution:
    def isHappy(self, n: int) -> bool:
        if n <= 0:
            return False 
        
        visited = set()
        
        while n != 1:
            n = self.getHappy(n);
            
            if n in visited:
                return False 
            
            else:
                visited.add(n)
                
        return True 
    
    
    def getHappy(self, n):
        ans = 0 
        while n > 0:
            ans += (n % 10) ** 2;
            n //= 10
            
        return ans 