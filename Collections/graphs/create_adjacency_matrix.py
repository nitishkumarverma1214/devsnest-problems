from collections import deque

def print_matrix (mat):
    for row in mat:
        print(*row)

def create_adj_matrix_directed(edges):
    n = 1+ max([e[0] for e in edges]+ [e[1] for e in edges])
    adj_matrix = [[0]*n for _ in range(n)]
    for e in edges:
        adj_matrix[e[0]][e[1]] = 1 
    
    return adj_matrix

def create_adj_matrix_undirected(edges):
    n = 1+ max([e[0] for e in edges]+ [e[1] for e in edges])
    adj_matrix = [[0]*n for _ in range(n)]
    for e in edges:
        adj_matrix[e[0]][e[1]] =adj_matrix[e[1]][e[0]]= 1 
    
    return adj_matrix
def BFS(adj_matrix):
    
    vis = set()
    n = len(adj_matrix)
    for i in range(n):
        if i in vis:
            continue
        
        vis.add(i)
        q = deque([i])
        while q:
            el = q.pop()
            print(el,end = " ")
            for ind,adj_el in enumerate(adj_matrix[el]):
                if adj_el and ind not in vis:
                    vis.add(ind)
                    q.appendleft(ind)
    print()

def DFS(adj_matrix):
    vis = set()
    n = len(adj_matrix)
    for i in range(n):
        if i in vis:
            continue
        
        vis.add(i)
        q = deque([i])
        while q:
            el = q.pop()
            print(el,end = " ")
            for ind,adj_el in enumerate(adj_matrix[el]):
                if adj_el and ind not in vis:
                    vis.add(ind)
                    q.append(ind)
    print()


def detect_cycle_undirected_bfs(adj_matrix):
    vis = set()
    n = len(adj_matrix)
    for i in range(n):
        if i in vis:
            continue
        vis.add(i)
        q = deque([[i,-1]])
        while q:
            el,par = q.pop()
            for adj_el in range(n):
                if adj_matrix[el][adj_el] :
                    if adj_el not in vis:
                        vis.add(adj_el)
                        q.appendleft([adj_el,el])
                    elif adj_el !=par:
                        print(f'cycle detected between {el}-{adj_el}')
                        return 
    print("No cycle")

def detect_cycle_undirected_dfs(adj_matrix):
    vis = set()
    n = len(adj_matrix)
    for i in range(n):
        if i in vis:
            continue
        vis.add(i)
        st = deque([[i,-1]])
        while st:
            el,par = st.pop()
            for adj_el in range(n):
                if adj_matrix[el][adj_el] :
                    if adj_el not in vis:
                        vis.add(adj_el)
                        st.append([adj_el,el])
                    elif adj_el !=par:
                        print(f'cycle detected between {el}-{adj_el}')
                        return 
    print("No cycle")

def recursive_dfs(adj_matix,vis,el,par):
    n = len(adj_matix)
    vis.add(el)
    for adj_el in range(n):
        if adj_matix[el][adj_el]:
            if adj_el not in vis:
                if recursive_dfs(adj_matix,vis,adj_el,el):
                    return True 
            elif adj_el !=par:
                print(f'cycle detected between {el}-{adj_el}')
                return True 
        
    return False

def detect_cycle_recursive_dfs(adj_matrix):
    vis = set()
    n = len(adj_matrix)
    for i in range(n):
        if i in vis:
            continue 
        
        if recursive_dfs(adj_matrix,vis,i,-1):
            return 
        
    print('No Cycle')

def directed_recursive_dfs(adj_matrix,vis,path,el):
    vis.add(el)
    path.add(el)

    for adjele in range(len(adj_matrix)):
        if adj_matrix[el][adjele]:
            if adjele not in vis:
                if directed_recursive_dfs(adj_matrix,vis,path,adjele):
                    return True 
                elif adjele in path:
                    print(f'cycle exits between {el}-->{adjele}')
                    return True 
    path.remove(el)
    return False     

def detect_cycle_directed_dfs_recursive(adj_matrix):
    vis = set()

    n = len(adj_matrix)
    for i in range(n):
        if i in vis:
            continue
        
        
        if directed_recursive_dfs(adj_matrix,vis,set(),i):
            return 
    
    print('No Cycle')


def main():
    edges = [(0,1),(1,3),(1,2),(3,4),(2,4),(5,7),(7,6)]
    undirected_graph = create_adj_matrix_undirected(edges)
    directed_graph= create_adj_matrix_directed(edges)
    # BFS(directed_graph)
    # DFS(directed_graph)
    # BFS(undirected_graph)
    # DFS(undirected_graph)
    # detect_cycle_undirected_bfs(undirected_graph)
    # detect_cycle_recursive_dfs(undirected_graph)
    detect_cycle_directed_dfs_recursive(directed_graph)

if __name__ == '__main__':
    main()