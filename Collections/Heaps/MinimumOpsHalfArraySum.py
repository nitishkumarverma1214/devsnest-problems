import heapq
from typing import List 
class Solution:
    def halveArray(self, nums: List[int]) -> int:
        s = sum(nums)
        nums = [-x for x in nums]
        heapq.heapify(nums) # maxHeap 
        
        no_of_ops = 0
        cur_sum =s
        while cur_sum>s/2 :
            no_of_ops +=1 
            ele = heapq.heappop(nums)
            ele = ele /2
            cur_sum += ele 
            heapq.heappush(nums,ele)
        return no_of_ops 
        
def main():
    nums = [1]
    print(Solution().halveArray(nums))
if __name__=="__main__":
    main()
    