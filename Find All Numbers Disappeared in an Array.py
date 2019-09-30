class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        numset = set(nums);
        ans = []
        for i in range(1, len(nums) + 1):
            if i not in numset:
                ans.append(i)
                
                
        return ans
        