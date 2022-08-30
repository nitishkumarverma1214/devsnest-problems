

res = []
#approach 1
def generate_permutation(arr,s,marked):
    for i in range(1,len(arr)+1):
        if len(s)==len(arr):
            res.append(s[:])
            return 

        if not marked[i]:
            s.append(arr[i-1])
            marked[i] = True 
            generate_permutation(arr,s,marked)
            s.pop()
            marked[i] = False

#approach 2:
def permutations(arr,pos=0):
    #when position is greater than length
    if pos>len(arr)-1:
        res.append(arr[:])
        return 
    for i in range(pos,len(arr)):
        arr[i],arr[pos] = arr[pos] , arr[i]
        permutations(arr,pos+1)
        arr[i],arr[pos] = arr[pos] , arr[i]

    
def main():
    n =3
    arr = list(range(1,n+1))
    print(arr)
    # generate_permutation(arr,[],[False]*(n+1))
    permutations(arr,0)
    print(res)
    
if __name__ == '__main__':
    main()