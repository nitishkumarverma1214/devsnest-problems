from collections import deque
import math

from Tree import TreeNode,print_tree
from array_to_levelorderTree import createTree

def maxWidth(root):
    
    maxw = 0
    q = deque([(root,0),None])
    st = []
    while q:
        
        x = q.popleft()
        
        if x:
            st.append(x[1])
            if x[0].left:
                q.append((x[0].left,x[1]*2+1))
            if x[0].right:
                q.append((x[0].right,x[1]*2+2))

             
        else:
            maxw = max(maxw,st[-1]-st[0]+1)
            st = []
            if q:
                q.append(None)

        
            
    return maxw +1
   


def main():
    arr =  [1,2,3,4,5,None,8,None,None,None,None,6,7]
    root = createTree(arr,None)
    #print_tree(root)
    print(maxWidth(root))
   
if __name__=="__main__":
    main()
