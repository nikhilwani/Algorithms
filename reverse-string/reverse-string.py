class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        #s.reverse()
        
        def helper(start, end, ss):
            
            # Base
            if start >= end:
                return 
            
            # Logic
            temp     = ss[start]
            ss[start] = ss[end]
            ss[end]   = temp
            
            helper(start+1, end-1, ss)
            
        helper(0, len(s)-1, s)
            
            
        