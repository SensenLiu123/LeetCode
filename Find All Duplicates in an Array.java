class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        
        //Map<Integer, Integer> freq = new HashMap<Integer, Integer>();
        
        List<Integer> ans = new ArrayList<Integer>();
        
        for (int i = 0; i < nums.length; i ++) {
            
            int cur = nums[i];
            cur = Math.abs(cur);
            
            if (nums[cur - 1] < 0){
                ans.add(cur);
                continue;
                
            } else {
                nums[cur - 1] = -1 * nums[cur - 1];
            }
            
        }
        
        return ans;
        
    }
}