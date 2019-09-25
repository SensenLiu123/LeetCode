# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        return self.dfs(root, p)
    
    def dfs(self, node, p):
        if node is None:
            return None 
        
        if p.val >= node.val:
            return self.dfs(node.right, p)
        
        else:
            left = self.dfs(node.left, p)
            
            if left:
                return left
            else:
                return node