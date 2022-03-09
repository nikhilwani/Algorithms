# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        self.res = False
        
        # TargetSum is not global. We need it in helper()
        self.targetsum = targetSum
        
        if root == None:
            return False
        
        self.helper(root, 0)
        
        return self.res 
    
    def helper(self, root, currsum):
        
        # Base
        if root == None:
            return
        # Logic
        currsum = currsum + root.val 
        
        # currsum is passed by reference. General recursion, not backtracking.
        self.helper(root.left, currsum)
        self.helper(root.right, currsum)
        
        if root.left == None and root.right == None:
            if currsum == self.targetsum:
                self.res = True
                
        
        
        
'''
        self.res = []
        self.helper(root)
        
        print("PREORDER")
        self.preorder(root)
        
        print("POSTORDER")
        self.postorder(root)
        
        return self.res
    
    def helper(self, root):
        
        if root == None:
            return 
        
        self.helper(root.left)
        print("UP")
        print(root.val)
        
        
        self.helper(root.right)
        print("DOWN")
        print(root.val)
        
    def preorder(self, root):
        
        # Base
        if root == None:
            return
        
        print(root.val)
        self.preorder(root.left)
        self.preorder(root.right)
        
    def postorder(self, root):
        
        # Base
        
        if root == None:
            return 
        
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.val)
'''

    