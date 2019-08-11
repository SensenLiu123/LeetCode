class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        if not S:
            return []
        
        res = []
        self.dfs(S, 0, '', res)
        
        return res 
    
    def dfs(self, S, i ,path, res):
        if i == len(S):
            res.append(path)
            return 
        
        if S[i].isdigit():
            self.dfs(S, i + 1, path + S[i], res)
            
        else:
            lower, upper = S[i].lower(), S[i].upper()
            self.dfs(S, i + 1, path + lower, res)
            self.dfs(S, i + 1, path + upper, res)