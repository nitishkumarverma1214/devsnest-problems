def quicksort(arr,start,end):
    if start>= end:
        return
    pindex = partition(arr,start,end)
    print("array after finding partition: ",arr)
    print("partition index :%d and element: %d" %(pindex, arr[pindex]))
    quicksort(arr,start,pindex-1)
    quicksort(arr,pindex,end)

def partition(arr,start,end):
    pivot =arr[end]
    pindex = start
    for i in range (start,end):
       if arr[i] <=pivot:
           arr[i],arr[pindex]= arr[pindex],arr[i]
           pindex +=1
    arr[end],arr[pindex] = arr[pindex],pivot
    return pindex


arr = [21,4,15,91,2,9]
print("array before quicksort: ",arr)
quicksort(arr,0,len(arr)-1)
print("array after quicksort: ",arr)