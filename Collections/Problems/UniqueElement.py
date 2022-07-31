def unique_element(arr,low,high,n):
    if n==0:
        return arr[0]
    if low<=high:
        mid = low+ (high-low)//2


        if (mid ==0 and arr[mid+1] !=arr[mid]) or (mid == n and arr[mid-1] != arr[mid]):
            return arr[mid]
        
        if arr[mid] == arr[mid-1] or arr[mid] ==arr[mid+1]:
            left = unique_element(arr,low,mid-1,n)
            if left:
                return left
            right = unique_element(arr,mid+1,high,n)

            return right

        else:
            return arr[mid]  


arr = [1]
n = len(arr)-1
print(unique_element(arr,0,n,n))