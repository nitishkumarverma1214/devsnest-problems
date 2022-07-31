def issorted(arr,start,arrlength):
    if start==arrlength-1:
        return True
    if arr[start]>arr[start+1]:
        return False
    return issorted(arr,start+1,arrlength)

arr=[1,2,3,7,4,5,6]
print(issorted(arr,0,len(arr)))

print(id(arr))
print(id(arr[2:]))
print(id(arr[3:]))
print(id(arr[5:]))