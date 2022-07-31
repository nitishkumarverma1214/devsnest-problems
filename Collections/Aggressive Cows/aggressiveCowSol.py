def binary_search(noOfStalls, noOfCows, stalls, mid):
   
   # selecting the first stall to place the first cow and decreasing the no of cow
    prev_stall_pos = 0
    noOfCows -=1

    for i in range(1,noOfStalls):

        if (stalls[i] - stalls[prev_stall_pos] >= mid):
            prev_stall_pos = i
            noOfCows -=1

            # When we place all the cow in the stall
            if not noOfCows:
                return True
    
    return False



def aggressiveCows(stalls,k):
    low = 1
    # maximum distance of last - first stall
    high = stalls[-1]-stalls[0]
    maximum_dist = 0
    noOfStalls = len(stalls)
    while (low<=high):
        mid = low + (high-low)//2
        
        if binary_search( noOfStalls, k, stalls, mid):
            low = mid+1
            if mid > maximum_dist:
                maximum_dist = mid
            
        else:
            high = mid-1

    return maximum_dist




    
    