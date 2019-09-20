class Solution:
    def countSubstrings(self, s: str) -> int:
        
        if len(s) == 0 or len(s) == 1:
            return 1 
        
        
        ans = 0 
        
        n = len(s)
        
        dp = [[0] * n for i in range(n) ] 
        
        for right in range(n):
            for left in range(right + 1) :
                if s[left] == s[right]:
                    if right - left <= 2 or dp[left + 1][right - 1] == 1:
                        dp[left][right] = 1 
                        ans += 1                 
                
        return ans 
        