class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        if "" in wordSet:
            wordSet.remove("")
            
            
        if len(s) == 0:
            return []
        if not wordSet:
            return []
        
        memo = {}
        return self.memoi(s, wordSet, memo)
    
    
    
    def memoi(self, s, wordSet, memo):
        if s in memo:
            return memo[s]
        
        if len(s) == 0:
            return []
        
        path = []
        if s in wordSet:
            path.append(s)
        
        for i in range(len(s)):
            if s[:i] not in wordSet:
                continue
            substring = s[:i]
            
            for combi in self.memoi(s[i:], wordSet, memo):
                path.append(substring + ' ' + combi)
        
        
        memo[s] = path
        return path 
        