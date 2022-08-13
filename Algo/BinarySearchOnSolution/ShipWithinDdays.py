from typing import List 
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def condition(weights, value) -> bool:
            c=0 
            s=0 
            for weight in weights:
                if weight+s<=value:
                    s+=weight 
                else:
                    s= weight 
                    c+=1 
            return (c+1)<=days 

        left, right = max(weights),sum(weights)
        ans =0 

        while left <= right:
            mid = left + (right - left) // 2
            if condition(weights,mid):
                ans = mid 
                right = mid-1 
            else:
                left = mid + 1
        return ans 


if __name__=="__main__":
    weights = [1,2,3,1,1]; days = 4
    print(Solution().shipWithinDays(weights ,days))