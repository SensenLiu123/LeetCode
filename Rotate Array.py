class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        
        self.reverse(nums, 0, len(nums) -1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) -1)
        return 
        
        
        
    def reverse(self, arr, start, end):
        left, right = start, end;
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1 
            right -= 1 
        