class Solution {
    public int mySqrt(int x) {
        if (x < 2) {
            return x;
        }
        
        int start = 1, end = x / 2; 
        long sqr;
        
        while (start + 1 < end) {
            int mid = start + (end - start) / 2;
            
            sqr = (long) mid * mid;
            
            if (sqr == x) {
                
                return mid;
                
            } else if (sqr > x){
                
                end = mid;
                
            } else {
                
                start = mid;
                
            }
        }
        
        sqr = (long) end * end;
        if (sqr > x) {
            return start;
        } 
        
        return end;
        
            
            
    }
}