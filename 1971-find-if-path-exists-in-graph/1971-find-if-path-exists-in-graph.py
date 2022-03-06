from collections import defaultdict
from collections import deque

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        adjlist = defaultdict(list)
        visited = set()
        path = []
        
        
        for v1, v2 in edges:
            adjlist[v1].append(v2)
            adjlist[v2].append(v1)
            
        queue = deque([source])
        
        while queue:
            
            current = queue.popleft()
            visited.add(current)
            
            for node in adjlist[current]:
                if node not in visited:
                    queue.append(node)
            
        if destination in visited:
            return True
        else:
            return False
            
            
            
        