class Solution {
    public int lengthOfLIS(int[] nums) {
        int n = nums.length;
        
        if (n == 0){
            return 0;
        }
        
        int[] dp = new int[n];
        for (int i = 0; i < n; i ++){
            dp[i] = 1;
        }
        
        int longest = 1;
        for (int i = 1; i < n; i ++){
            for (int prev = 0; prev < i; prev ++){
                if (nums[i] <= nums[prev]){
                    continue;
                }
                dp[i] = Math.max(dp[i], dp[prev] + 1);
                longest = Math.max(longest, dp[i]);
            }
        }
        return longest;
    }
}