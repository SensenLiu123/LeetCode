# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, s: int) -> bool:
        all_sums = set()
        
        self.dfs(root, 0, all_sums)
        
        return s in all_sums 
            
            
    def dfs(self, root, rolling, all_sums):
        if root is None:
            return 0 
            
        if root.left:
            self.dfs(root.left, rolling + root.val, all_sums)
            
        if root.right:
            self.dfs(root.right, rolling + root.val, all_sums)
            
            
        if not root.left and not root.right:
            all_sums.add(rolling + root.val)
            return 
        