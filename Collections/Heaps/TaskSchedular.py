import heapq
from typing import List 
from collections import Counter,deque

class Solution:
    def taskSchedular(self,tasks:List[str], n: int)->int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)
        q = deque() 
        time = 0 
        while maxHeap or q :
            time +=1 
            if maxHeap:
                processEle = heapq.heappop(maxHeap)
                processEle +=1 
                if processEle:
                    q.append((processEle,time+n))
            
            if q and  q[0][1] == time:
                heapq.heappush(maxHeap ,q.popleft()[0])
        
        return time 

        



if __name__=="__main__":
    tasks = ['A','A','A','B','B','B']
    n=2 
    print(Solution().taskSchedular(tasks,n))