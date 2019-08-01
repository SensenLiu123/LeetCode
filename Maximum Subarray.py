class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        if len(nums) == 0:
            return 0 
        
        if len(nums) == 1:
            return nums[0]
        
        prefixSum = 0
        
        minSum = 0
        ans = -2 ** 31
        for number in nums:
            
            prefixSum += number 
            
            ans = max(ans, prefixSum - minSum)
            
            minSum = min(minSum, prefixSum)
            
        return ans 
            
        