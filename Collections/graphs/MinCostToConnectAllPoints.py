import heapq
def solve(points):
    dist = []
    n = len(points)
    for x in range(n):
        for y in range(x+1,n):
            dist.append((abs(points[x][0]-points[y][0])+abs(points[x][1]-points[y][1]),x,y))
    heapq.heapify(dist)
    mstsum =0
    par=[i for i in range(n)]
    while n>1:
        d,x,y = heapq.heappop(dist)
        parx,pary = par[x],par[y]
        while parx != par[parx]:
            parx = par[parx]
        while pary != par[pary]:
            pary = par[pary]
        if parx != pary:
            mstsum+=d
            n-=1
            par[parx] = pary 
    return mstsum


def main():
    
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    
    print(solve(points))
if __name__ == '__main__':
    main()