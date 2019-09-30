class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        int n = nums.length;
        int [] visited = new int [n];
        
        for (int i = 0; i < n; i ++){
            int cur = nums[i];
            
            visited[cur - 1] = 1;
        }
        
        List<Integer> ans = new ArrayList<Integer>();
        for (int i = 0; i < n; i ++){
            if (visited[i] == 0){
                
                ans.add(i + 1);
            }
            
        }
        
        
        return ans;
    }
}