class Solution {
    public boolean isAnagram(String s, String t) {
        
        if (s.length() != t.length()){
            return false; 
        }
        int [] anaS = new int [26];
        int [] anaT = new int [26];
        
        
        for (int i = 0; i < s.length(); i ++) {
            anaS[s.charAt(i) - 'a'] ++;
            anaT[t.charAt(i) - 'a'] ++;
        }
        
        
        for (int i = 0; i < 26; i ++) {
            if (anaS[i] != anaT[i]){
                return false;
            }
        }
        return true;
        
    }
}