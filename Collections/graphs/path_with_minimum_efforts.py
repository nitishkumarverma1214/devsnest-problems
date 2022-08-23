from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        def condition(k,vis,x,y,m,n):
            if x==m-1 and y ==n-1:
                return True
            vis.add((x,y))
            dir=[(0,1),(0,-1),(1,0),(-1,0)]
            res = False
            for _x,_y in dir:
                new_x = x+_x
                new_y = y+_y 
                if -1<new_x<m and -1<new_y<n and (new_x,new_y) not in vis and abs(heights[x][y] - heights[new_x][new_y])<=k:
                    res = res or condition(k,vis,new_x,new_y,m,n)
                if res:
                    return res 
            return res 
        left, right = 0,1000000
        ans =0 
        m= len(heights)
        n = len(heights[0])
        while left <= right:
            mid = left + (right - left) // 2
            if condition(mid,set(),0,0,m,n):
                ans = mid 
                right = mid-1 
            else:
                left = mid + 1
        return ans 


def main():
    heights = [[1,2,2],[3,8,2],[5,3,5]]
    print(Solution().minimumEffortPath(heights))
    
if __name__ == '__main__':
    main() 