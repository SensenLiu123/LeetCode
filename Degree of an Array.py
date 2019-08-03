class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        leftIdx, rightIdx = {}, {}
        count = {}
        
        for i, number in enumerate(nums):
            if number not in leftIdx:
                leftIdx[number] = i 
                
            rightIdx[number] = i
            count[number] = count.get(number, 0) + 1 ;
            
        
        ans = len(nums)
        degree = max(count.values())
        
        for value in count:
            if count[value] == degree:
                ans = min(ans, rightIdx[value] - leftIdx[value] + 1)
                
                
        return ans 
        