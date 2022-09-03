from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        cur = []
        res = []
        def f(pos):
            if pos == len(nums):
                res.append(cur[:])
                return 
            
            
            cur.append(nums[pos])
            f(pos+1)
            cur.pop()
            f(pos+1)
        
        f(0)
        return res

def main():
    print(Solution().subsets([1,2,3]) )
if __name__ == '__main__':
    main()