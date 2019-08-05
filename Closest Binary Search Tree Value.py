# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if root is None:
            return -1 
        
        upper = self.getUp(root, target)
        lower = self.getLow(root, target)
        
        if lower is None:
            return upper.val
        if upper is None:
            return lower.val
            
        if target - lower.val < upper.val - target:
            return lower.val
        return upper.val
    
    def getUp(self, node, target):
        if node is None:
            return None
        
        if node.val <= target:
            return self.getUp(node.right, target)
        
        upper = self.getUp(node.left, target);
        return node if not upper else upper 
        
    def getLow(self, node, target):
        if node is None:
            return None 
        
        if node.val > target:
            return self.getLow(node.left, target)
        
        lower = self.getLow(node.right, target)
        
        return node if lower is None else lower
        
    
        