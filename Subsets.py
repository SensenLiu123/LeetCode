class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        
        result = []
        
        self.dfs(nums, 0, [], result)
        
        return result 
    
    def dfs(self, nums, i, path, result):
        
        if i > len(nums):
            return 
        
        result.append(path[:])a
        
        for i in range(i, len(nums)):
            path.append(nums[i])
            
            self.dfs(nums, i + 1, path, result)
            
            path.pop()
            
        
            
            