SIZE = 111111
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m, n = len(needle), len(haystack)
        
        if m == 0:
            return 0 
        
        if m > n:
            return -1 
        
        if m == n and needle == haystack:
            return 0
        
        needleHash = 0 
        hayHash = 0
        
        power =  1 ;
        
        for char in needle:
            needleHash = (needleHash * 31 + ord(char) ) % SIZE
            power *= 31
            power %= SIZE
            
        for i in range(m):
            hayHash = (hayHash * 31 + ord(haystack[i]) ) % SIZE
            
        
        for start in range(n - m + 1):
            if needleHash == hayHash and self.sameString(needle, haystack, start , m):
                return start 
            else:
                # move this window
                newComer = start + m;
                if newComer >= n:
                    break;
                hayHash = (hayHash * 31 + ord(haystack[newComer]) ) % SIZE 
                
                hayHash -= (ord(haystack[start]) *power) % SIZE;
                if hayHash < 0:
                    hayHash += SIZE 
                    
        return -1  
    
    def sameString(self, nee, hay, i ,m):
        return nee == hay[i: i + m];
                
        
        