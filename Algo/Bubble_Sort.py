def bubble_sort(arr):
    length= len(arr)
    for i in range(length-1):
        for j in range(length-i-1):
            if arr[j]> arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
        print("array after ",i+1," iteration: ",arr)

arr = [21,4,1,3,9,20,25,6,21,14,0]
bubble_sort(arr)