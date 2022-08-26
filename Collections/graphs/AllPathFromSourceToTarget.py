from  typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n= len(graph)
        curpath=[0]
        ans = []
        def path():
            if curpath[-1] == n-1:
                ans.append(list(curpath))
                return
            
            for el in graph[curpath[-1]]:
                curpath.append(el)
                path()
                # print(curpath)
                curpath.pop()
        path()
        return ans
def main():
    
    graph = [[1,2],[3],[3],[]]
    
    print(Solution().allPathsSourceTarget(graph))
if __name__ == '__main__':
    main()