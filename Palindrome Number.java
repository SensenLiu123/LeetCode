class Solution {
    public boolean isPalindrome(int x) {
        
        if (x < 0){
            return false ;
        }
        
        if (x == 0) {
            return true;
        }
        
        int origin = x ; 
        int symtry = 0 ; 
        
        
        while (x > 0){            
            symtry = symtry * 10 + x % 10 ;
            
            x /= 10;
        }
        
        return origin == symtry ; 
        
    }
}