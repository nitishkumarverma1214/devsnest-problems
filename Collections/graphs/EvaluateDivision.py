from typing import List
def dfs(g,src,dest,vis):
    p = g[src]
    vis.add(src)
    if dest in p:
        return p[dest]
    for key in p:
        
        if key not in vis:
            a= dfs(g,key,dest,vis)
            
            if a!=-1:
                return a*p[key]
    return -1
    
class Solution:
       def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
            g = {}
            res = []
            for i in range(len(equations)):
                if equations[i][0] in g:
                    g[equations[i][0]].update({equations[i][1]:values[i]})


                else:
                    g[equations[i][0]] = {equations[i][1]:values[i]}

                if equations[i][1] in g:
                        g[equations[i][1]].update({equations[i][0]:1/values[i]})
                else:
                    g[equations[i][1]] ={equations[i][0]:1/values[i]}

            for q in queries:
                if q[0] not in g or q[1] not in g:
                    res.append(float(-1))
                else:
                    if q[0]==q[1]:
                        res.append(float(1))
                    else:
                        res.append(float(dfs(g,q[0],q[1],set())))



            return res



def main():
   


    equations = [["x1","x2"],["x2","x3"],["x3","x4"],["x4","x5"]]
    values = [3.0,4.0,5.0,6.0]
    queries =[["x1","x5"],["x5","x2"],["x2","x4"],["x2","x2"],["x2","x9"],["x9","x9"]]
    print(Solution().calcEquation(equations,values,queries))
    
if __name__ == '__main__':
    main()