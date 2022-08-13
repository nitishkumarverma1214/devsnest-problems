import math
from typing import List 
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        
        def canEat(k):
            hours = 0 
            for pile in piles:
                hours+= math.ceil(pile/k)
            
            return hours<=h 
                
        
        
        left = 1
        right = max(piles)
        ans = 1 
        
        while left<=right:
            mid = left+(right-left)//2 
            if canEat(mid):
                ans = mid 
                right= mid-1
            else:
                left=mid+1 
        return ans 

if __name__=="__main__":
    piles = [3,6,7,11]; h = 8
    print(Solution().minEatingSpeed(piles,h))