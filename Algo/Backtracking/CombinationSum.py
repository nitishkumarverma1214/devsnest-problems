from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cursum = 0
        leftover = sum(candidates)
        res = []
        cur = []
        n = len(candidates)
        def dfs(cursum,leftover,pos):
            if cursum ==target:
                res.append(cur[:])
                return 
            if cursum>target or cursum+leftover < target:
                return 
            
            for i in range(pos,n):
                ele = candidates[i]
                cursum +=ele
                leftover -= ele
                cur.append(ele)
                dfs(cursum,leftover,pos)
                pos+=1 
                cursum -=ele
                leftover += ele
                cur.pop()
                
        dfs(cursum,leftover,pos=0)
        return res 
if __name__ == '__main__':
    print(Solution().combinationSum([1],2))