class Solution {
    public int firstUniqChar(String s) {
        if (s.length() == 0 | s == null){
            return -1;
        }
        
        Map<Character, Integer> freq = new HashMap<Character, Integer>();
        
        for (int i = 0; i < s.length(); i ++){
            char c = s.charAt(i);
            if (freq.containsKey(c)){
                
                freq.put(c,freq.get(c) + 1);
                
            } else {
                freq.put(c, 1);
            }
        }
        
        for (int i = 0; i < s.length(); i ++){
            char c = s.charAt(i);
            if (freq.get(c) == 1){
                return i;
            } 
        } 
        return -1;
    }
}