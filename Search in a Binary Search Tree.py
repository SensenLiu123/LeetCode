# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        return self.dfs(root, val) ;
    
    
    def dfs(self, node, val):
        if node is None:
            return None 
        
        if val > node.val:
            return self.dfs(node.right, val)
        
        if val < node.val:
            return self.dfs(node.left, val)
        else:
            return node
        