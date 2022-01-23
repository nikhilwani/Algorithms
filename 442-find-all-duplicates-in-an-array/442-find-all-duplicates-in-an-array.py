from collections import Counter

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
#         result = []
        
#         for val in nums:
#             if nums.count(val) == 2:
#                 if val not in result:
#                     result.append(val)
#         return result
 

        counter = Counter(nums)
        result = []   
        
        for val in counter:
            if counter[val] == 2:
                result.append(val)
        
        return result
            