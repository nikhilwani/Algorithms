from collections import defaultdict
from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        nodes = [*range(n)]
        adj_list = {n:[] for n in nodes}
        
        #adj_list = defaultdict(list)
        visited  = set()
        component = 0 
        
        for e1, e2 in edges:
            adj_list[e1].append(e2)
            adj_list[e2].append(e1)
        
        
        for node in adj_list.keys():
            
            if node not in visited:
                component += 1
                
                queue = deque([node])
                
                while queue:
                    current = queue.popleft()
                    visited.add(current)

                    for neighbors in adj_list[current]:
                        if neighbors not in visited:
                            queue.append(neighbors)
        
        return component
                
                
                
        