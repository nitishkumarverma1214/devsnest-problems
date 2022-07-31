def printmatrix(arr):
    for eachlist in arr:
        for eachelement in eachlist:
            print(eachelement,end="\t")
        print()

arr=[[1],[2],[3]]
#arr = [[1,2,3]]
#arr = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
printmatrix(arr)
k = 0; l = 0
m = len(arr)
n = len(arr[0])
res = []
print("Spiral Matrix : ")
while (k < m and l < n):
    for i in range(l, n):
        res.append(arr[k][i])
    k += 1
    for i in range(k, m):
        res.append(arr[i][n-1])    
       
    n -= 1
    if ( k < m):
        for i in range(n-1,(l-1),-1):
            res.append(arr[m-1][i])
        m -= 1
    if (l < n):
        for i in range(m-1,k-1,-1):
            res.append(arr[i][l])
        l += 1
print(res)

