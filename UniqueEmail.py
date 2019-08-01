class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        
        distinctEmails = set()
        
        for email in emails:
            newName = self.process(email) ; 
            
            distinctEmails.add(newName) ; 
            
        return len(distinctEmails) ; 
    
    
    def process(self, email):
        atIdx = email.index('@')
        ans = ''
        
        for i in range(atIdx):
            if email[i] == '.':
                continue
            
            if email[i] == '+':
                break 
                
            ans += email[i]
            
        ans += email[atIdx :]
        
        return ans
        
# It is important to keep @ in the new string 

test = Solution()
emails = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]

print(test.numUniqueEmails(emails)) 


                
            
                
            
            
            