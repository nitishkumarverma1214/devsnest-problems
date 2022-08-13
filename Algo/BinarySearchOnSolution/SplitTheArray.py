from typing import List 
class Solution:
    def countSubArray(self,nums,maxSubArraySum):
        c =0 
        s = 0 
        for num in nums:
            if s+num <=maxSubArraySum:
                s+=num
            else:
                s =num 
                c+=1 
        return c +1
       
        
        
    def splitArray(self, nums: List[int], m: int) -> int:
        low = max(nums)
        high = sum(nums)
        ans = high 
        
        while low<high:
            mid = low+(high-low)//2 
            count = self.countSubArray(nums,mid)
            if count<=m:
                ans = min(ans,mid)
                high = mid-1 
            else:
                low =mid+1 
        return ans 
        



if __name__=="__main__":
    nums = [7,2,5,10,8]
    m = 2
    print(Solution().splitArray(nums,m))