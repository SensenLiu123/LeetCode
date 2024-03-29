# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0
        self.dfs(root)
        return root 
    
    
    def dfs(self, root):
        if root is None:
            return 
        
        self.dfs(root.right)
        
        self.sum += root.val
        root.val = self.sum
        
        self.dfs(root.left)
        