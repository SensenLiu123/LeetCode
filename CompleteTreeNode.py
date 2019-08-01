# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0 

        height = self.getHeight(root) ;

        if height == 1:
         	return 1 

         #count number of leaves 
        leaveCount = self.bsFind(root, height) ;

         # full above tree is. 2^(h-1) - 1	

        return 2 ** (height - 1) - 1 + leaveCount ;


    def getHeight(self, root):
    	height = 0 
    	node = root 

    	while node:
    		height += 1 
    		node = node.left

    	return height


    def bsFind(self, root, h):
    	# return number of leaves in the tree 
    	# Binary search 

    	start, end = 0, 2 ** (h-1) - 1 

    	while start + 1 < end:
    		mid = start + (end - start) // 2 

    		if self.exist(root, mid, h):
    			start = mid 
    		else:
    			end = mid 


    	return start + 1 

    def exist(self, node, guess, h):
    	left, right = 0 , 2 ** (h-1) - 1 ; 

    	for layer in range(1, h + 1 ):
    		mid = (left + right) // 2

    		if guess > mid:
    			node = node.right
    			left = mid + 1 

    		else:
    			node = node.left 
    			right = mid 

    	return node is not None 


