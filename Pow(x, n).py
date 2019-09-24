class Solution:
    def myPow(self, x: float, n: int) -> float:
        if abs(x) < 0.0000001:
            return 0 
        
        if n == 0:
            return 1 
        
        if n == 1:
            return x 
        
        if n < 0:
            return self.myPow(1.0 / x, -n );
        
        
        res = 1 
        power = x 
        while n > 0:
            if n % 2 == 1:
                res *= power 
                
            power *= power 
            
            n //= 2
            
        return res 