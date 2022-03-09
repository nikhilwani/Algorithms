# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
#     global rootsum
#     rootsum = 0 
    
#     def sumNumbers(self, root: Optional[TreeNode]) -> int:
#         # this works! We are not assigning value to a global variable.
#         #print(rootsum)
        
#         if root == None:
#             return 0
        
#         self.helper(root, 0)
        
#         return rootsum
        
        
#     def helper(self, root, cursum):
#         #print(rootsum)
#         # since we are assinging a global variable.
#         global rootsum
        
#         if root == None:
#             return 
        
#         cursum = 10 * cursum + root.val
        
        
#         self.helper(root.left, cursum)
        
#         if root.left == None and root.right == None:
#             rootsum = rootsum + cursum
        
        
#         self.helper(root.right, cursum)
            
            
# '''  
#     def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
#         rootsum = 0 

#         if root == None:
#             return 0
        
        
        
#         def helper(self, root, cursum):

#             if root == None:
#                 return 

#             cursum = 10 * cursum + root.val
            
#             helper(self, root.left, cursum)

#             if root.left == None and root.right == None:
#                 rootsum = rootsum + cursum


#             helper(self, root.right, cursum)
        

#         helper(self, root, 0)
        
#         return rootsum
        
# '''
        
        
  
    #global rootsum

    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        
        self.rootsum = 0 
        #print(rootsum)
        if root == None:
            return 0
        
        self.helper(root, 0)
        
        return self.rootsum
        
        
    def helper(self, root, cursum):
        
        if root == None:
            return 
        
        cursum = 10 * cursum + root.val
        
        
        self.helper(root.left, cursum)
        
        if root.left == None and root.right == None:
            self.rootsum = self.rootsum + cursum
        
        
        self.helper(root.right, cursum)
           