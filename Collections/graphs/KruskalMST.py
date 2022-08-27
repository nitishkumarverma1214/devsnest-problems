
import heapq

par =[]
def find(el):
    if el!=par[el]:
        par[el]= find(par[el])
    return par[el]
def union(x,y):
    parx = find(x)
    pary = find(y)
    if parx!=pary:
        par[parx] = pary
        return True
    else:
        return False


def kruskal(noOfNodes,graph):
    minheap = [(w,i,j)  for i in range(len(graph)) for j,w in graph[i].items()]
    heapq.heapify(minheap)
    minCost =0
    itr = noOfNodes
    while itr>1:
        d, x,y = heapq.heappop(minheap)
        if union(x,y):
            minCost+=d
            itr-=1

    return minCost

def main():
    noOfNodes = 6
    global par
    par = [i for i in range(noOfNodes)]
    graph = [{1:10,4:20,5:40},{0:10,2:50,5:60},{1:50,3:30,5:90},{2:30,4:80,5:70},{0:20,3:80,5:40},{0:40,1:60,2:90,3:70,4:40}]
    print(kruskal(noOfNodes,graph))

if __name__ == '__main__':
    main()