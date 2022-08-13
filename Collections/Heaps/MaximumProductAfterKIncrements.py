import heapq
from typing import List 
from functools import reduce
class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        while k:
            el = heapq.heappop(nums)
            heapq.heappush(nums,el+1)
            k-=1 
        return reduce(lambda a,b: ( ( a % 1000000007 ) * ( b % 1000000007 ) ) % 1000000007,nums)

if __name__=="__main__":
    nums = [6,3,3,2]
    k = 2
    print(Solution().maximumProduct(nums,k))