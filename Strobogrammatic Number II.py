pair = {'0':'0', '1':'1', '6':'9', '9':'6','8':'8'}

class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n == 1:
            return ['0','1','8']
        
        strobo = self.helper(n)
        
        ans = []
        for string in strobo:
            if string[0] == '0':
                continue 
                
            ans.append(string)
        return ans 
    
    
    def helper(self, n):
        ans = []
        if n == 0:
            return ans
        
        if n == 1:
            return ['0','1','8'] 
        
        if n == 2:
            for k in pair:
                ans.append(k + pair[k])
            return ans 
        
        prev = self.helper(n - 2)
        for k in pair:
            for stro in prev:
                ans.append(k + stro + pair[k])
                
        return ans 
                
                
        
        
        
        
        
            