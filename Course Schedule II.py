class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        if numCourses == 0:
        	return []

        if numCourses == 1:
        	return [0]

        indegree , neighbors = self.getGraph (prerequisites, numCourses) ; 

        startNodes = []
        for node in indegree:
        	if indegree[node] == 0:
        		startNodes.append(node)

        res = []
        if len(startNodes) == 0:
        	return res  

        queue = collections.deque(startNodes);
        

        while queue:
        	node = queue.popleft()
        	res.append(node)

        	for nextCourse in neighbors[node]:
        		indegree[nextCourse] -= 1 

        		if indegree[nextCourse] == 0:
        			queue.append(nextCourse)


        return res if len(res) == numCourses else []

        def getGraph(self, prerequisites, N ):
    	indegree = {x : 0 for x in range(N)}

    	neighbors = {x:[] for x in range(N)}

    	for pair in prerequisites:
    		root = pair[1]
    		leave = pair[0]

    		indegree[leave] += 1 
    		neighbors[root].append(leave)


    	return indegree, neighbors