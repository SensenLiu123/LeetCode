class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if len(word) == 0:
            return abbr =='0'
        
        i, j = 0, 0
        
        while i < len(word) and j < len(abbr):
            if abbr[j].isalpha():
                if abbr[j] != word[i]:
                    return False 
                
                else:
                    i += 1
                    j += 1
                                        
            else: # we meet a digit 
                if abbr[j] == '0':
                    return False 
                count = 0
                while j < len(abbr) and abbr[j].isdigit():
                    count = count * 10 + int(abbr[j])
                    j += 1 
                    
#                 if count == 0:
#                     return False 
                
                i += count                 
                
        return i == len(word) and j == len(abbr) 