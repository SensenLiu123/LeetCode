# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0 
        
        return self.dfs(root)
    
    
    def dfs(self, node):
        if node is None:
            return 0
        
        leftH = self.dfs(node.left)
        rightH = self.dfs(node.right)
        
        return max (leftH, rightH) + 1 
        