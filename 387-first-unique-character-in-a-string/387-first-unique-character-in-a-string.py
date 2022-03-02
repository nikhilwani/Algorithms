from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        if len(s) == 0:
            return -1
        
        counter = Counter(s)
        
        for i, char in enumerate(s):
            if counter[char] == 1:
                return i
        
        return -1
        
        
        
        '''
        
        hashtable = {}
        
        
        # Use collections.Counter instead to build the couter.
        for char in s:
            try:
                hashtable[char] = hashtable[char] + 1
            except:
                hashtable[char] = 1
                
        
        for char in s:
           if hashtable[char] == 1:
            return s.index(char)
        
        return -1
        
        '''