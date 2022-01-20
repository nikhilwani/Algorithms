# from collections import deque
class Solution:
    # Time Complexity - O(m*n)
    # Space Complexity - O(m*n)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if grid is None or len(grid) == 0:
            return 0
        m = len(grid)
        n = len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        q = deque()
        fresh = 0
        # Loop through the matrix and find all the fresh and rotten oranges.
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        if fresh == 0:
            return 0

        time = 0
        while len(q):
            qLen = len(q)
            for i in range(qLen):
                curr = q.popleft()
                for direction in directions:
                    new_row = curr[0] + direction[0]
                    new_col = curr[1] + direction[1]
                    if new_row >= 0 and new_row < m and new_col >= 0 and new_col < n and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        fresh -= 1
                        q.append((new_row, new_col))
            time += 1

        if fresh != 0:
            return -1
        return time - 1
    
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        if grid == None or len(grid) == 0 or grid[0] == None or len(grid[0]) == 0:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        
        fresh = 0
        time  = 0
        
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = []
        
        
        for i in range(0, m):
            for j in range(0, n):
                
                
                if grid[i][j] == 1:
                    fresh = fresh + 1
                    
                if grid[i][j] == 2:
                    queue.append(i)
                    queue.append(j)
                    
        print("afer for")
        print(queue)
        print(fresh)
        if fresh == 0:
            return 0
        
        while queue:
            size = len(queue)
            

            for i in range(0, size, 2):
                r = queue.pop()
                c = queue.pop()
                
                for dir_ in dirs:
                    nr = r + dir_[0]
                    nc = c + dir_[1]
                    
                    if nr >= 0 and nc >=0 and nr < m and nc < n and grid[nr][nc] == 1:
                        
                        queue.append(nr)
                        queue.append(nc)
                        fresh = fresh - 1
                        grid[nr][nc] = 2    
                        
            time = time + 1
                
        if fresh != 0:
            return -1
        
        return time

'''