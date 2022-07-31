def first_occurance(arr,start,num):

    if len(arr) == start:
        return -1 # num not found

    if arr[start]==num:
        return start
    
    return first_occurance(arr,start+1,num)
def last_occurance(arr,start,num):
    if start ==len(arr):
        return -1
    res =last_occurance(arr,start+1,num)
    if res!=-1:
        return res

    if arr[start] == num:
        return start
    return -1


arr=[1,3,4,2,3,4,2,3,5,6]
index = first_occurance(arr,start=0,num=3)
print(index)

index = last_occurance(arr,start=0,num=3)
print(index)