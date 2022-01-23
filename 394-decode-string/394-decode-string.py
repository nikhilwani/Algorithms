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
                num = ((num * 10) + int(c) )
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
        