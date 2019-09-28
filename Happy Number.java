class Solution {
    public boolean isHappy(int n) {
        if (n <= 0) {
            return false;
        }
        
        Set<Integer> visited = new HashSet<Integer> ();
        
        while (n != 1) {
            n = getHappy(n);
            
            if (visited.contains(n)){
                return false; 
            } else {
                visited.add(n);
            }
            
        }
        return true;
    }
    
    private int getHappy(int n){
        int ans = 0;
        
        while (n > 0){
            ans += (n % 10) * (n % 10);
                
            n /= 10;
        }
        
        return ans;
    }
}