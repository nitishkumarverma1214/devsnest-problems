# worst case time complexcity = O(nlogn)
# space complexcity of O(n) auxillary

def mersort(arr):
    length = len(arr)
    if length< 2:
        return arr
    
    mid=length//2
    L= arr[:mid]  # 0 to mid-1
    R= arr[mid:]  # mid to  end
    print("L: ",L,"  R: ",R)
    mersort(L)
    mersort(R)
    merge(L,R,arr)
    print (" arr: ",arr )

def merge(L,R,arr):
    print ("merge: ",L,R)
    len_left=len(L)
    len_right=len(R)

    i=j=k=0
    while i<len_left and j<len_right:
        if L[i] <= R[j]:
            arr[k]=L[i]
            i+=1
            
        else:
            arr[k] = R[j]
            j+=1
        
        k+=1
    
    # remaining array elements
    while i<len_left:
        arr[k]=L[i]
        i+=1
        k+=1
    
    while j<len_right:
        arr[k] = R[j]
        k+=1
        j+=1

arr = [21.4,1,3,9,20,25]
print("array Before sort: ",arr)
mersort(arr)
print("array after sort: ",arr)