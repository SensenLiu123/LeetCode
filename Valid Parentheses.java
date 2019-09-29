class Solution {
    public boolean isValid(String s) {
        if (s == null | s.length() == 0){
            return true;
        }
        
        Map<Character, Character> pair = new HashMap<Character, Character> ();
        
        pair.put(')','(');
        pair.put(']','[');
        pair.put('}','{');
        
        Stack<Character> stack = new Stack<Character>();
        
        for (int i = 0; i < s.length(); i ++){
            char sym = s.charAt(i);
            
            if (pair.containsValue(sym)){
                stack.push(sym);
            } else {
                
                if (stack.isEmpty()){
                    return false;
                }
                    
                char left = stack.pop();
                if (left != pair.get(sym)){
                    return false;
                }    
                
            }
        }
        return stack.isEmpty();
        
    }
}