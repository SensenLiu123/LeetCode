# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        stack = []
        preorder = []
        
        if root is None:
            return preorder
        
        stack.append(root)
        
        while stack:
            node = stack.pop()
            
            preorder.append(node.val)
            
            if node.right:
                stack.append(node.right)
                
            if node.left:
                stack.append(node.left)
                
        return preorder
        
        