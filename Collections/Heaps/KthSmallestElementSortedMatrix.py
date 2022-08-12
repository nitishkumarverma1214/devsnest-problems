import heapq
from typing import List 


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        maxHeap = []
        for row in matrix:
            for el in row:
                if len(maxHeap)<k:
                    heapq.heappush(maxHeap,-el)
                else:
                    if maxHeap[0]< -el :
                        heapq.heappop(maxHeap)
                        heapq.heappush(maxHeap,-el)
                        
        return -maxHeap[0]
if __name__=="__main__":
    matrix = [[1,5,9],[10,11,13],[12,13,15]]
    k = 8
    print(Solution().kthSmallest(matrix,k))