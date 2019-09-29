class Solution {
    public boolean isOneEditDistance(String s, String t) {
        int longL = s.length();
        int shortL = t.length();
        
        if (shortL > longL){
            return isOneEditDistance(t ,s);
        }
        
        if (longL - shortL > 1){
            return false;
        }
        
        for (int i = 0; i < shortL; i ++) {
            if (s.charAt(i) != t.charAt(i)){
                
                if (shortL == longL){
                    return s.substring(i + 1).equals(t.substring (i + 1));
                } else {
                    return s.substring(i + 1).equals(t.substring(i) );
                }
                
            }
        }
        
        return longL == shortL + 1;
    }
}