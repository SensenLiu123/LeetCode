class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        prefix = 0 
        
        modCount = {0:1}
        
        for number in A:
            newMod = (prefix + number) % K ;
            modCount[newMod] = modCount.get(newMod, 0) + 1 
            prefix = newMod 
            
        return sum(v*(v-1) // 2 for v in modCount.values())
            
        
        