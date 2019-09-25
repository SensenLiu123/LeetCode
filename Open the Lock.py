import collections 
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends);
        if '0000' in dead:
            return -1 
        queue = collections.deque(['0000'])
        dist = {'0000': 0}
        
        while queue:
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                
                if cur == target:
                    return dist[cur]
                
                for nex in self.turn(cur) :
                    if nex in dist or nex in dead:
                        continue 
                    queue.append(nex)
                    dist[nex] = dist[cur] + 1 
                    
        return -1 
    
    def turn(self, s):
        ans = []
        
        for i in range(4):
            newChar1 = str ( (int(s[i]) + 1) % 10 ) 
            newChar2 = str ( (int(s[i]) + 9) % 10 ) 
            ans.append(s[:i] + newChar1 + s[i + 1:])
            ans.append(s[:i] + newChar2 + s[i + 1:])
            
        return ans 