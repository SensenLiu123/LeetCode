class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if (len(nums) == 0):
            return 0
        
        pool = set(nums);
        maxStreak = 0;
        
        for num in nums:
            if num not in pool:
                continue;
            
            # num in pool
            # a new streak
            streak = 1;
            pool.remove(num)
            l = num - 1;
            r = num + 1;
            while l in pool:
                pool.remove(l)
                streak += 1;
                l -= 1 
                
            while r in pool:
                pool.remove(r);
                streak += 1;
                r += 1;
                
            maxStreak = max(maxStreak, streak);
            
            
        return maxStreak;
            
                
        
        