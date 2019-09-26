# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        return self.dfs(root)
    
    
    def dfs(self, node):
        if node is None:
            return 0 
        
        if not node.left:
            return self.dfs(node.right) + 1
        if not node.right:    
            return self.dfs(node.left) + 1
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        return min(left, right) + 1
        
        