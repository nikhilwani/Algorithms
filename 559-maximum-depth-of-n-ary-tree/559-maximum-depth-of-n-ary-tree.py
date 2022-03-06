"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
from collections import deque

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        
        if root == None:
            return 0
        
        levels = []
        level = 0 
        
        
        queue = deque([root])

        while queue:
            
            levels.append([])
            len_q = len(queue)
            
            for i in range(len_q):
                current = queue.popleft()
                
                levels[level].append(current.val)
                
                if current.children:
                    queue.extend(current.children)
            
                
            level += 1
            
        return len(levels)
                
        
        