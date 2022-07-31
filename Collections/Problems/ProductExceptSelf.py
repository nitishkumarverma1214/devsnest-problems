def productExceptSelf(arr):
    size = len(arr)
    ans = [1] * size
    lp =1; rp =1

    for ind in range(1,size):
        lp *=arr[ind-1]
        rp *=arr[size-ind]
        ans[ind] =ans[ind] * lp
        ans[size-ind-1] = ans[size-ind-1] * rp
    return ans

arr = [1,2,3,4,5]

print(productExceptSelf(arr))
