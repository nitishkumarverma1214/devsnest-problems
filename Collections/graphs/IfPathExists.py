from collections import deque,defaultdict
from typing import List 
def create_adj_matrix(edges,n):
    adj = defaultdict(list)
    for e in edges:
        adj[e[0]].append(e[1])
        adj[e[1]].append(e[0])
        
    return adj 
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True 
        adj = create_adj_matrix(edges,n)
        vis = set([source])
        q = deque([source])

        while q:
            el = q.pop()
            
            for adjel in range(n):
                if adjel in adj[el]:
                    if adjel == destination:
                        return True 
                    elif adjel not in vis:
                        vis.add(adjel)
                        q.appendleft(adjel)

        return False 
def main():
    edges = [(0,1),(0,2),(3,5),(5,4),(4,3)]
    print(Solution.validPath(edges=edges,n=6,source=0,destination=5))

if __name__ == '__main__':
    main()