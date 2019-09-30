class Solution:
    def firstUniqChar(self, s: str) -> int:
        if len(s) == 0:
            return -1; 
        
        
        charFreq = {};
        for char in s:
            charFreq[char] = charFreq.get(char, 0) + 1;
            
            
        for i in range(len(s)):
            if charFreq[s[i]] != 1:
                continue;
            else:
                return i;
            
            
        return -1; 
        
        