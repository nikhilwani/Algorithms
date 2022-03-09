# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    
    #global rootsum
    
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.rootsum = 0 
        #print(rootsum)
        if root == None:
            return 0
        
        self.helper(root, 0)
        
        return self.rootsum
        
        
    def helper(self, root, cursum):
        print(self.rootsum)
        if root == None:
            return 
        
        cursum = 10 * cursum + root.val
        
        
        self.helper(root.left, cursum)
        
        if root.left == None and root.right == None:
            self.rootsum = self.rootsum + cursum
        
        
        self.helper(root.right, cursum)