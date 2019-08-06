# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None:
            root = TreeNode(val)
            return 
        
        return self.helper(root, val); 
    
    def helper(self, node, val):
        if node is None:
            node =  TreeNode(val);
            return node
        
        if val <= node.val:
            node.left = self.helper(node.left, val)
            
        else:
            node.right = self.helper(node.right, val )
            
        return node 