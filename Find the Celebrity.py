# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return -1 
        
        candidate = 0 
        
        for i in range(n):
            if i == candidate or knows(i,candidate):
                continue 
                
            if not knows(i , candidate):
                candidate = i
                
                
        for i in range(n):
            if i == candidate:
                continue 
                
            if not knows(i, candidate):
                return -1 
            
            if knows(candidate, i):
                return -1 
            
            
        return candidate 
            
        
        