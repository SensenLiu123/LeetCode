"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None:
            return 0
        
        
        return self.dfs(root)
    
    def dfs(self, node):
        if node is None:
            return 0 
        
        maxHeight = 0 
        for child in node.children:
            maxHeight = max(self.dfs(child), maxHeight)
            
        return maxHeight + 1 ;
            