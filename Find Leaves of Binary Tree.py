# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        heightNode = {}
        maxH = self.dfs(root, heightNode)
        ans = []
        
        for i in range(1, maxH + 1):
            if i in heightNode:
                ans.append(heightNode[i])
                
                
        return ans 
        
        
    def dfs(self, node, heightNode):
        if node is None:
            return 0 
        
        
        left = self.dfs(node.left, heightNode)
        right = self.dfs(node.right, heightNode)
        h = max(left, right) + 1 
        
        if h in heightNode:
            heightNode[h].append(node.val)
        else:
            heightNode[h] = [node.val]
            
        return h
        