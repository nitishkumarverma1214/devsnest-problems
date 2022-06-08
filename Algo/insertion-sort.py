def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        value = arr[i]
        j=i-1
        while (j>-1):
            if arr[j] >value:
                arr[j+1] = arr[j]
            else:
                break
            j-=1
        arr [j+1] = value
        print("array: ",i," pass: ",arr)



arr = [7,4,6,2]
print("array before sort: ",arr)
insertion_sort(arr)
print("array after sort: ",arr)