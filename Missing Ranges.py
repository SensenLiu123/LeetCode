class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        
        if lower > upper:
            return []
        
        if len(nums) == 0:
            if lower == upper:
                return [str(lower)]
            else:
                return [str(lower) + '->' + str(upper)]
            
        ans = []    
        for i in range(len(nums)):
            if i == 0:
                string = self.getInterval(lower - 1, nums[i])
                if string:
                    ans.append(string)
            if i == len(nums) - 1:
                string = self.getInterval(nums[i], upper + 1)
                
            else:
                string = self.getInterval(nums[i], nums[i + 1])
                
            if string:
                    ans.append(string)
                    
                    
        return ans 
    
    
    def getInterval(self, low, high):
        if high - low > 2:
            return str(low + 1) + '->' + str(high - 1)
        
        if high - low == 2:
            return str(low + 1)
        
        
        else: 
            return ""
            