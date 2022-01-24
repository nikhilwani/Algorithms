class Solution:
    
    dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        if grid == None or len(grid) == 0:
            return 0 
        
        m = len(grid)
        n = len(grid[0])
        
        
        count = 0 
        
        for i in range(m):
            for j in range(n):
                
                if grid[i][j] == '1':
                    count = count + 1
                    
                    self.dfs(grid, i, j, m, n)    
       
        return count     
                    
        
    def dfs(self, grid, r, c, m, n):
    
        # Base
        if (r < 0 or c < 0 or r == m or c == n or grid[r][c] != '1'):
            return 
        
        # Logic
        grid[r][c] = '0'
        
        for dir_ in self.dirs:
            i = r + dir_[0]
            j = c + dir_[1]
            
            self.dfs(grid, i, j, m, n)
    
    
    
    
''' 
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        rows, cols = len(grid), len(grid[0])
        q, visit = collections.deque(), set()    
        islands = 0
        
        def bfs(r, c):
            q.append((r, c))
            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if ( r in range(rows) and c in range(cols) and
                        grid[r][c] == "1" and (r, c) not in visit 
                       ):
                        q.append((r, c))
                        visit.add((r, c))
                        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        return islands    
'''