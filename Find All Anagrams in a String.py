class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        if len(p) == len(s):
            return [0] if s == p else []
        
        s_map,p_map = {},{}
        for i in range(len(p)):
            s_map[s[i]] = s_map.get(s[i],0) + 1 
            p_map[p[i]] = p_map.get(p[i],0) + 1 
            
                
        ans = []    
        if s_map == p_map:
            ans.append(0)
            
        for window_start in range(1, len(s) - len(p) + 1):
            window_end = window_start + len(p) -1 
            s_map[s[window_end]] = s_map.get(s[window_end],0) + 1
            
            s_map[s[window_start - 1]]-= 1 
            if s_map[s[window_start - 1]] ==0:
                del s_map[s[window_start - 1]]
            
            if s_map == p_map:
                ans.append(window_start)
                
        return ans 
                
        