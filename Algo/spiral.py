def printmatrix(arr):
    for eachlist in arr:
        for eachelement in eachlist:
            print(eachelement,end="\t")
        print()


def spiralOrder(matrix):
    res = []
    n = len(matrix)
    m = len(matrix[0])
    
    dir=0
    top =0
    down = n-1
    left =0
    right = m-1
    
    while top <= down and left <= right:

        # left to right
        if (dir == 0):
            for i in range( left,right+1):
               
                res.append(matrix[top][i])
            top +=1
        # Top to bottom
        elif (dir ==1):
            for j in range(top,down+1):
                res.append(matrix[j][right])
            right -=1
        
        # right to left
        elif dir ==2:
            for l in range(right,left-1,-1):
                res.append(matrix[down][l])
            down -=1
        # bottom to top
        elif dir ==3:
            for a in range(down,top-1,-1):
                res.append(matrix[a][left])
            left +=1
        
        dir = (dir+1)%4
       
    
   
    return res
    


num =1
row =1
col =3
arr = []
for r in range(row):
    l=[]
    for c in range(col):
        
        l.append(num)
        num+=1
    arr.append(l)
arr = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
printmatrix(arr)
#expectedarr = [1,2,3,7,11,10,9,5,6 ]
#print("\nExpected output:",expectedarr)

actualarr = spiralOrder(arr)
print("\nActual output:  ",actualarr)

