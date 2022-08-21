
from collections import deque


def create_adj_matrix_directed(edges):
    n = 1+ max([e[0] for e in edges]+ [e[1] for e in edges])
    adj_matrix = [[0]*n for _ in range(n)]
    for e in edges:
        adj_matrix[e[0]][e[1]] = 1 
    
    return adj_matrix

def topological_sort(adj_mat):
    vis=set()
    n = len(adj_mat)
    inorder = [0]*n 

    # calculate inorder of each vertex 
    for row in range(n):
        for col in range(n):
            if adj_mat[row][col]:
                inorder[col]+=1 
    q = deque()
    for node,order in enumerate(inorder):
        if not order:
            q.appendleft(node)

    while q:
        el = q.pop()
        print(el,end=" ")

        for adjel in range(n):
            if adj_mat[el][adjel]==1:
                inorder[adjel]-=1 
                if not inorder[adjel]:
                    q.appendleft(adjel)

def main():
    edges = [(0,1),(1,2),(0,2),(3,1),(4,1),(6,0),(5,2)]
    directed_graph= create_adj_matrix_directed(edges)
    topological_sort(directed_graph)
    
if __name__ == '__main__':
    main()