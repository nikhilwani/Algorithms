
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        
        res = []
        
        if root == None:
            return []
        
        queue = deque([root])
        
        while queue:
            
            len_q = len(queue)
            
            for i in range(len_q):
                current = queue.popleft()
                
                
                if current.left and current.right:
                    queue.append(current.left)
                    queue.append(current.right)
                    
                else:
                    if current.left:
                        res.append(current.left.val)
                        queue.append(current.left)
                    
                    if current.right:
                        res.append(current.right.val)
                        queue.append(current.right)
                        
        return res
                         
                        
                    
            
                    
                
            
        
        