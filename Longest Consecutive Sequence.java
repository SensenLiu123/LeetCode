class Solution {
    public int longestConsecutive(int[] nums) {
        if (nums.length == 0){
            return 0;
        }
        
        Set<Integer> pool = new HashSet<>();
        
        for (int i = 0; i < nums.length; i ++) {
            pool.add(nums[i]);
        }
        
        int ans = 0; 
        for (int i = 0; i < nums.length; i ++){
            if (!pool.contains(nums[i])) {
                continue;
            }
            int streak = 1, x = nums[i];
            pool.remove(x);
            int l = x - 1, r = x + 1;
            while (pool.contains(l)){
                pool.remove(l);
                streak ++;
                l --;
            }
            
            while (pool.contains(r)){
                pool.remove(r);
                streak ++;
                r ++;
                
            }
            ans = Math.max(ans, streak);
        }
        return ans;
    }
}