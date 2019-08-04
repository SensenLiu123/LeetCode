# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        _, Yes = self.dfs(root) ;
        return Yes
        
    def dfs(self, node):
        if node is None:
            return 0, True
        
        leftD, leftYes = self.dfs(node.left)
        rightD, rightYes = self.dfs(node.right)
        
        if not leftYes or not rightYes:
            return 0, False 
        
        if abs(leftD - rightD) > 1:
            return 0, False 
        
        else:
            return max(leftD, rightD) + 1 , True 