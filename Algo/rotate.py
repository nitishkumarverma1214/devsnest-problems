""" when we rotate a 2d list two times once along the x -axis(180) and other along the diagonal we get a 
    matrix rotated by 90 degree of the original matrix.

    Real life usecase: A pricture is made up of small pixel (like 2d list), so its same as rotating the image
    by 90.
"""
def matrixprint(arr):
    for row in arr:
        for element in row:
            print(element,end="\t")
        print()

def rotate (matrix ) -> None:
    n = len(matrix)
    
    for index in range(n):
        top = 0
        bottom = n-1
        while top < n//2:
            matrix[top][index],matrix[bottom][index] = matrix[bottom][index],matrix[top][index]
            top+=1
            bottom -=1
    print("*********Rotate around x-axis**************")
    matrixprint(matrix)

    print("*********Rotate around diagonal axis******************")
    for outer in range(n):
        for inner in range(outer+1,n):
            matrix[outer][inner] ,matrix[inner][outer] = matrix[inner][outer],matrix[outer][inner]
    matrixprint(matrix)
    
arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print("Given array:")
matrixprint(arr)
rotate(arr)