# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        res = []
        
        def helper(root):
            #print("calling helper", root.val)
            
            if root == None:
                #print("here")
                return None
            
            if root.val == val:
                #print("found")
                res.append(root)
                return 
            
            if val < root.val:
                helper(root.left)

            if val > root.val:
                helper(root.right)
            
        helper(root)
        if res:
            return res[0]
        else:
            return None
        
        
            