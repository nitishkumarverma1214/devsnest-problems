par = [i for i in range(8)]
rank = [0]*8
# check if two elements belongs to same set or not (using path compression)
def find(ele):
    if ele!=par[ele]:
        par[ele] = find(par[ele])
    
    return par[ele] 


# union by rank: attach the tree with lower rank to tree with higher rank.
def union(ele1,ele2):
    par1 = find(ele1)
    par2 = find(ele2)
    if par1!=par2:
        if (rank[par1]<rank[par2]):
            par1,par2 = par2,par1 
        par[par2] = par1
        if rank[par1] ==rank[par2]:
            rank[par1]+=1 

def main():
    union(1,2)
    union(2,3)
    union(4,5)
    union(6,7)
    union(5,6)
    union(2,6)
    
if __name__ == '__main__':
    main()