
def heapifydown(arr,pos,size):
    while pos <size//2:
        c1,c2 = 2*pos+1, 2*pos+2 
        max_idx = pos 
        if c1<size and arr[c1]>arr[pos]:
            max_idx = c1 
        if c2 <size and arr[c2]>arr[max_idx]:
            max_idx = c2 
        
        if max_idx == pos :
            break
    
        arr[pos],arr[max_idx] = arr[max_idx],arr[pos]
        pos = max_idx

def createHeap(arr):
    for idx in range(len(arr)//2,-1,-1):
        heapifydown(arr,idx,len(arr))


def heapsort(arr):
    # One by one extract elements
    N = len(arr)
    for i in range(N-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # swap
        heapifydown(arr, 0, i)
 
    



if __name__=="__main__":
    arr = [1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17]
    createHeap(arr) # TC of O(n) using buttom up approach 
    print("Heap of array:",arr)
    heapsort(arr) # TC of O(nlogn)
    print("array after heapsort:",arr)