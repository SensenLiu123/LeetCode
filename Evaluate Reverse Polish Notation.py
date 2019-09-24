class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for s in tokens:
            if s not in '+-*/':
                stack.append(int(s))
                
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                res = self.calc(num1, num2, s)
                stack.append(res)
                
        return stack.pop()
    
    
    def calc(self, a, b, symbol):
        if symbol == '+':
            return a + b
        
        if symbol == '-':
            return a - b
        
        if symbol == '*':
            return a * b
        
        else:
            return int(1.0 * a / b)