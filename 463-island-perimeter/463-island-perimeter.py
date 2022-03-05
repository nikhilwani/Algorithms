from collections import deque

class Solution:
    
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        

        self.perimeter = 0 
        
        self.m = len(grid)
        self.n = len(grid[0])
        
        
        
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 1:
                    self.bfs(i,j, grid)
                    
        return self.perimeter 
                    
        
        
    def bfs(self, r, c, grid):
        print("here")
        # to get our neighbors
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        visited = set()

        queue = deque()
        queue.append([r, c])
        visited.add((r,c))


        while queue:


            len_queue = len(queue)

            print("here")
            for i in range(len_queue):
                node = queue.popleft()

                #print(node)
                for dirr in dirs:
                    nr = dirr[0] + node[0]
                    nc = dirr[1] + node[1]
                    
                    print("current", node[0], node[1])
                    print(nr, nc)
                    
                    if (nr < 0 or nc < 0 or nr == self.m or nc == self.n):
                        print(nr, nc, "if: inside ++ permiter")
                        self.perimeter += 1
                        
                    else:
                        if grid[nr][nc] == 0:
                            print(nr, nc, "else: inside ++ permiter")
                            self.perimeter += 1

                    if (nr >= 0 and nc >= 0 and nr < self.m and nc < self.n and grid[nr][nc] == 1 and (r, c) not in visited):
                        queue.append([r, c])
                    
            
        
        
        
        
        
        