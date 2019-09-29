class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        if abs( len(s) - len(t) ) > 1:
            return False; 
        
        m , n = len(s), len(t)
        if m >= n:
            longer = s;
            shorter = t;
        else:
            longer = t;
            shorter = s;
            
        for i in range(len(shorter)):
            if longer[i] != shorter[i]:
                
                if m == n:
                    return longer[i + 1:]  == shorter[i + 1:];
                
                else:
                    
                    return longer[i + 1:] == shorter[i:];
                
                
        return len(longer) - len(shorter) == 1;
    
    
    
        