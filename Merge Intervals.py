class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) == 0 or not intervals:
            return []
        
        intervals.sort(key = lambda x: (x[0], x[1]) ) 
        ans = []
        prev = None
        
        
        for cur in intervals:
            if not prev or cur[0] > prev[1]:
                ans.append(cur)
                prev = cur
                continue
                
            if cur[1] > prev[1]:
                prev[1] = cur[1]
                continue
                
                
        return ans 
                
                
            