
def print_matrix (mat):
    for row in mat:
        print(*row)
def create_wt_directed_graph(noOfnodes,edges,wt):
    n = noOfnodes
    wt_mat = [[0]*n for _ in range(n)]
    for ind in range(len(edges)):
        x,y = edges[ind]
        wt_mat[x][y] =  wt[ind]
    
    return wt_mat

def create_wt_undirected_graph(noOfnodes,edges,wt):
    n = noOfnodes
    wt_mat = [[0]*n for _ in range(n)]
    for ind in range(len(edges)):
        x,y = edges[ind]
        wt_mat[x][y] =wt_mat[y][x]=  wt[ind]
    return wt_mat 

# prerequist: positive weighted matrix 
def dijkstra(adj):
    n = len(adj)
    dist = [float('inf')]*n
    vis = [False]*n 

    # distance of source from source is zero
    dist[0] = 0 

    for i in range(n):

        # select the vertex from non- Actual Shortest path with min distance
        x = -1 
        mindist = float('inf')
        for node in range(n):
            if not vis[node] and dist[node]<mindist:
                x = node 
                mindist = dist[node] 
        
        vis[x] = True 

        # relax the node which are connected to the visited node 
        for adjel in range(n):
            if adj[x][adjel] >0 and not vis[adjel]:
                dist[adjel] = min(dist[adjel],adj[x][adjel]+ dist[x])

    
    # minimun distance from source
    print("source \t vertex")
    for dis in dist:
        print("0 \t "+str(dis))


def main():
    n=7
    edges = [(0,1),(0,2),(1,2),(1,3),(2,3),(3,4),(3,5),(4,6),(5,6)]
    wts=[10,20,5,15,20,15,5,20,5]
    undirected_graph =create_wt_undirected_graph(n,edges,wts)
    directed_graph= create_wt_directed_graph(n,edges,wts)

    
    dijkstra(undirected_graph)
    #dijkstra(directed_graph)
if __name__ == '__main__':
    main()