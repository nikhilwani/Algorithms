class Solution:
    
    
    def single_rotate(self, s):
        rotated_s = s[1:] + s[0]
        
        return rotated_s
    
    def rotateString(self, s: str, goal: str) -> bool:
        rotations = [s]
        
        for i in range(len(s) - 1):
            rotations.append(self.single_rotate(rotations[-1]))
        
        print(rotations)
        if goal in rotations:
            return True
        else:
            return False
        
        
        
        
        
