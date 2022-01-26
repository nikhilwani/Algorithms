class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        answer = []
        rightindex = []
        leftindex = []
        
    
        
        leftsum = 0
        rightsum = 0 
        
        leftindex.append(leftsum)
        rightindex.append(rightsum)
    
        #print(leftindex, rightindex)
        
        for i in range(1, len(nums)):
            leftsum = leftsum + nums[i - 1]
            leftindex.append(leftsum)
            
        print(leftindex)
        

        for j in reversed(range(0, len(nums) - 1)):
            
            rightsum = rightsum + nums[j + 1]
            rightindex.append(rightsum)
    
  
        rightindex.reverse()
        
        print(rightindex) 
        
        x = 0 
        
        for i, j in zip(leftindex, rightindex):
            
            if i == j:
                return x
            
            x = x + 1
            
        return -1
                
            
            
            
        