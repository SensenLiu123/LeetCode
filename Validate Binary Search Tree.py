# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        _,_,Yes = self.dfs(root) ;
        return Yes 
    
    def dfs(self, node):
        if node is None:
            return None ,None, True 
        
        leftMax, leftMin, leftYes = self.dfs(node.left)
        rightMax, rightMin, rightYes = self.dfs(node.right)
        
        if not leftYes or not rightYes:
            return None , None, False 
        
        if rightMin and rightMin.val <= node.val:
            return None ,None ,False 
        
        if leftMax and leftMax.val >= node.val:
            return None, None, False 
        
        else:
            minNode = leftMin if leftMin else node 
            maxNode = rightMax if rightMax else node
            return maxNode, minNode, True 