def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = arr[i]
        min_index = i
        for j in range(i+1,n):
            if arr[j] < min:
                min = arr[j]
                min_index = j
        arr[i],arr[min_index] = min,arr[i]
        print("array after :",i+1, " pass: ", arr)

arr = [5,1,3,4,2]
print("array before sort: ",arr)
selection_sort(arr)
print("array after sort: ",arr)