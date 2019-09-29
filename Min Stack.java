class MinStack {
     
    /** initialize your data structure here. */
    
    Stack<Integer> nums = new Stack<Integer>();
    Stack<Integer> mins = new Stack<Integer>();
    
    public MinStack() {
        
    }
    
    public void push(int x) {
        nums.push(x);
        
        if (mins.empty()){
            mins.push(x);
            return;
        } 
        
        int top = mins.peek();
        if (top <= x){
            mins.push(top);
        } else {
            mins.push(x);
        }
        return;
        
    }
    
    public void pop() {
        if (nums.empty()){
            return;
        }
        nums.pop();
        mins.pop();
        
    }
    
    public int top() {
        if (nums.empty()){
            return -1;
        }
        
        return nums.peek();
        
    }
    
    public int getMin() {
        if (mins.empty()){
            return -1;
        }
        return mins.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */