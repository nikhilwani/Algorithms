class Solution:
    
    # Global variable
    i = 0
    
    def decodeString(self, s: str) -> str:
        if s == None or len(s) == 0:
            return s
        
        num = 0
        currstr = ""
        
        numstack = []
        strstack = []
        
        while self.i < len(s):
            #print("i", self.i)
            c = s[self.i]
            
            if c.isdigit():
                num = ((num * 10) + int(c))
                #print("num formed",num)
                self.i = self.i + 1
            
            # It is the child when '[' is detected.
            elif (c == '['):
                
                self.i = self.i + 1
                child = self.decodeString(s)
                newstr = ""
                
                for k in range(num):
                    newstr = newstr + child
                    
                currstr = currstr + newstr
                num = 0
                
                
            elif c == ']':
                self.i = self.i + 1
                return currstr
                
            else:
                currstr = currstr + c
                self.i = self.i + 1
        
        return currstr
        



'''
# Iterative 

class Solution:
    
    
    def decodeString(self, s: str) -> str:
        
        if s == None or len(s) == 0:
            return s
        
        num = 0
        currstr = ""
        
        numstack = []
        strstack = []
        
        for i in range(len(s)):
            print("i", i)
            c = s[i]
            
            if c.isdigit():
                num = ((num * 10) + int(c))
                print("num formed",num)
            
            elif (c == '['):
                print("num:",num)
                numstack.append(num)
                strstack.append(currstr)
                num = 0
                currstr = ""
            
            elif c == ']':
                print("here")
                
                times = numstack.pop()
                newstring = ""
                
                for i in range (times):
                    newstring = newstring + currstr
                
                parent = strstack.pop()
                currstr = parent + newstring 
                
            else:
                currstr = currstr + c
                
        
        
        return currstr
'''        