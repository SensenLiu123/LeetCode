class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) < 2:
            return []
        
        numPair = {}
        
        for i , number in enumerate(nums):
            
            if target - number not in numPair:
                numPair[number] = i
            else:
                res = [numPair[target - number] , i]
                return res 
                
                
        
            