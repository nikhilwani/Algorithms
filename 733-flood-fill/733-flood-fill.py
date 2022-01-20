class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        
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