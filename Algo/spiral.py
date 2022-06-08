def printmatrix(arr):
    for eachlist in arr:
        for eachelement in eachlist:
            print(eachelement,end="\t")
        print()


def spiralOrder(matrix):
    res = []
    n = len(matrix)
    
    k,ltr,ttb,rtl,bbt = 0,0,n-1,n-1,0
    while ltr < n//2:
        for i in range( k,n-1-k):
            res.append(matrix[ltr][i])
        for j in range(k,n-1-k):
            res.append(matrix[j][ttb])
        
        # need a fix
        for l in range(n-1-k,k,-1):
            #print("l is %d"%l)
            res.append(matrix[rtl][l])
        for m in range(n-1-k,k,-1):
            res.append(matrix[m][bbt])
        
        ltr +=1
        ttb -=1
        rtl -=1
        bbt+=1
        k+=1
    if n%2 !=0:
        res.append(matrix[n//2][n//2])
    return res
    


num =1
row =6
col =6
arr = []
for r in range(row):
    l=[]
    for c in range(col):
        
        l.append(num)
        num+=1
    arr.append(l)

printmatrix(arr)
#expectedarr = [1,2,3,7,11,10,9,5,6 ]
#print("\nExpected output:",expectedarr)

actualarr = spiralOrder(arr)
print("\nActual output:  ",actualarr)
