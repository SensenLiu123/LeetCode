class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        if k > len(nums):
            return 0 
        
        runningSum = 0
        
        for i in range(k):
            runningSum += nums[i]
           
        maxAve = runningSum * 1.0 / k 
        
        for start in range(1, len(nums) - k + 1):
            end = start + k - 1 
            
            runningSum += nums[end]
            runningSum -= nums[start - 1]
            
            maxAve = max(maxAve, runningSum * 1.0 / k)
            
            
        return maxAve
        
        
        
        