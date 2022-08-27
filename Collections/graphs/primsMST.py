
import heapq


def prims(noOfNodes,graph):
    lock = [True]*noOfNodes

    lock[0] = False
    minheap = [(w,v) for v,w in graph[0].items()] # ----O(E)
    edgeCount =0
    minCost =0
    heapq.heapify(minheap) #----O(E)
    while edgeCount<noOfNodes-1:
        cost,vertex = heapq.heappop(minheap)
        if lock[vertex]:
            edgeCount+=1
            minCost+=cost 
            lock[vertex] = False 
            for e,w in graph[vertex].items():
                heapq.heappush(minheap,(w,e))
    
    return minCost



def main():
    noOfNodes = 6
    graph = [{1:10,4:20,5:40},{0:10,2:50,5:60},{1:50,3:30,5:90},{2:30,4:80,5:70},{0:20,3:80,5:40},{0:40,1:60,2:90,3:70,4:40}]
    print(prims(noOfNodes,graph))

if __name__ == '__main__':
    main()