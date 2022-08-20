import heapq
from typing import List 
class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        piles = [-x for x in piles]
        heapq.heapify(piles)
        for _ in range(k):
            ele = heapq.heappop(piles)
            heapq.heappush(piles,-(-ele-(-ele//2)))
        
        return -sum(piles)


def main():
    piles = [4,3,6,7]; k = 3
    print(Solution().minStoneSum(piles,k))
if __name__=="__main__":
    main()
    