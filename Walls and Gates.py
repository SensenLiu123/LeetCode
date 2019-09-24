import collections
MOVES = [(0,1), (0,-1), (1, 0), (-1, 0)]
INF = 2147483647;
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        m = len(rooms)
        if m == 0:
            return 
        
        n = len(rooms[0])
        if n == 0:
            return 
        queue = collections.deque()
        distance = {}
        
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i,j))
                    distance[(i, j)] = 0
        
        #distance = -1            
        while queue:
            #distance += 1 
            for _ in range(len(queue)):
                x,y = queue.popleft()
                rooms[x][y] = distance[(x, y)] 
                
                for dx,dy in MOVES:
                    xx,yy = x+ dx, y+ dy
                    if (xx, yy) in distance:
                        continue 
                    if self.in_map_and_empty(rooms, xx, yy):
                        queue.append((xx,yy))
                        # rooms[xx][yy] = rooms[x][y] + 1
                        distance[(xx, yy)] = distance[(x, y)] + 1 

        return 
        
    def in_map_and_empty(self, rooms, x, y):
        m,n = len(rooms), len(rooms[0])
        return 0 <= x < m and 0 <= y < n and rooms[x][y] == INF
    
               
        
        