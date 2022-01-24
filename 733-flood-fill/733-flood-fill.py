class Solution:
    
    color = 0 
    dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    m = 0
    n = 0 
    
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        # BFS 
        if image == None or len(image) == 0 or image[sr][sc] == newColor:
            return image
         
        self.m = len(image)
        self.n = len(image[0])
        
        self.color = image[sr][sc]
        self.dfs(image, sr, sc, newColor)  
        
        return image

    def dfs(self, image, r, c, newColor):
        
        #base
        if r < 0 or c < 0 or r == self.m or c == self.n or image[r][c] != self.color: 
            return
        
        # logic
        image[r][c] = newColor
        
        for dirr in self.dirs:
            nr = r + dirr[0]
            nc = c + dirr[1]
            self.dfs(image, nr, nc, newColor)
    



'''



class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        # BFS 
        if image == None or len(image) == 0 or image[sr][sc] == newColor:
            return image
         
        m = len(image)
        n = len(image[0])
        
        color = image[sr][sc]
        queue = []
        queue.append([sr, sc])
        image[sr][sc] = newColor      
        
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        while queue:
            curr = queue.pop()
            for dir_ in dirs:
                
                # neighboring directions.
                nr = dir_[0] + curr[0]
                nc = dir_[1] + curr[1]
                
                if (nr >= 0 and nc >= 0 and nr < m and nc < n and image[nr][nc] ==  color ):
                        queue.append([nr, nc])
                        image[nr][nc] = newColor 
        
        
        return image
'''