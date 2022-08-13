def countSubArray(nums,minSweetness):
        c =0 
        s = 0 
        for num in nums:
            if s >=minSweetness:
                c+=1 
                s=num 
            else:
                s+=num 
        return c +1
       
def getMaximumSweetness(nums, k):
        low = 1
        high = sum(nums)
        ans = low   
        
        while low<=high:
            mid = low+(high-low)//2 
            count = countSubArray(nums,mid)
            if count<k+1:
                high = mid-1 
            else:
                ans = max(ans,mid)
                low =mid+1 
        return ans 
        






if __name__=="__main__":
    nums = [5, 6 ,7, 8, 9, 10, 11, 12 ,13]
    k = 3
    print(getMaximumSweetness(nums,k))