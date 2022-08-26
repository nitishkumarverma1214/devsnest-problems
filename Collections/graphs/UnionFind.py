#union find is used to find no of disjoint set, cycle detection, 

def find_union(noOfNodes,edges):
    par = [x for x in range(noOfNodes)]

    for edge in edges:
        node_a, node_b = edge[0],edge[1]
        par_a,par_b = node_a,node_b 

        while par_a != par[par_a]:
            par_a = par[par_a]
        
        while par_b != par[par_b]:
            par_b = par[par_b]
        
        if par_a!=par_b:
            par[par_a] = par_b 
        
        else:
            print('Already Connected!!!')
            return 
        
