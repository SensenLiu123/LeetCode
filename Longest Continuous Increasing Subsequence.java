class Solution {
    public int findLengthOfLCIS(int[] nums) {
        int n = nums.length;
        if (n == 0){
            return 0;
        }
        int longest = 1;
        int streak = 1;
        for (int i = 1; i < n; i ++){
            if (nums[i] <= nums[i-1]){
                streak = 1;
                //continue;
            } else {
                streak ++;
            }
            
            longest = Math.max(longest, streak);
        
        }
        
        return longest;
    }
}