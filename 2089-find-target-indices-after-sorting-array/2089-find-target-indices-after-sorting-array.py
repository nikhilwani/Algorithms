class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        idxs = []
        actual_nums = nums.sort()
         
        for i, num in enumerate(nums):
            if num == target:
                idxs.append(i)
        
            
        
#         # count of non target values
#         c_nt = 0 
        
#         # count of target value. 
#         c_t = 0
        
#         idxs = []
        
#         for num in nums:
#             if num == target:
#                 c_t = c_t + 1
            
#         c_nt = len(nums) - c_t
        
#         print(c_nt)
#         print(c_t)
#         if c_t > 1:
            
#             while c_t > 0:
#                 idxs.append(c_nt - 1)
#                 c_nt = c_nt - 1
#                 c_t = c_t - 1
                
#         if c_t == 1:
#             print("here")
#             while c_t > 0:
#                 idxs.append(c_nt - c_t)
#                 c_nt = c_nt - 1
#                 c_t = c_t - 1


    
        
        
            
            
        
        return idxs
        