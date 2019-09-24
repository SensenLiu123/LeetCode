class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        if len(num) == 0:
            return False 
        
        origin = self.str2num(num)

        original = origin
        if origin < 0:
            return False 
        
        if origin == 0:
            return True 
        
        strobo = {1:1, 6:9, 9:6, 8:8, 0:0}
        
        newNum = 0
        while origin > 0:
            digit = origin % 10
            if digit not in strobo:
                return False 
            newNum = newNum * 10 + strobo[digit]
            origin //= 10
            
            
        return newNum == original
    
    
    def str2num(self, s):
        ans = 0
        for char in s:
            if not char.isdigit():
                return -1
            
            ans = ans * 10 + int(char)
            
        return ans
            
            
            
            
        
        
        
        
        
    