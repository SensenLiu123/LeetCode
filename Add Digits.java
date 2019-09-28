class Solution {
    public int addDigits(int num) {
        if (num <= 0){
            return 0; 
        }
        
        Map<Integer, Integer> visited = new HashMap<Integer, Integer>();
        
        while (num > 9){
            num = adding(num, visited); 
        }
        
        return num;
        
    }
    
    
    
    private int adding(int num, Map<Integer, Integer> visited) {
        
        if (visited.containsKey(num)) {
            int res = visited.get(num);
            return res;
        }
        
        int res = 0; 
        int copy = num;
        
        while (num > 0){
            
            res += num % 10;
            
            num /= 10;
        }
        
        visited.put(copy, res);
        return res;
    }
}