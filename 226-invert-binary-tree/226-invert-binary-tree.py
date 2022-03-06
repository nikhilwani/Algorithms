# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        
        if root == None:
            return root
        
        queue = deque([root])
        
        while queue:
            
            
            
            temp = TreeNode(None, None, None)
            current = queue.popleft()
            
            if current.left or current.right:
                temp = current.left
                current.left = current.right
                current.right = temp 
            
            
            if current.left:
                queue.append(current.left)
            
            if current.right:
                queue.append(current.right)
            
        return root 
        
        
        
        