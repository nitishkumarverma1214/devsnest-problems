from collections import deque
import math
from Tree import TreeNode,print_tree
from array_to_levelorderTree import constructTreeLevelOrder

def maxWidth(root):
    if not root:
        return root 
    level = 0
    maxw = 1
    
    q = deque([root,None])
    while q:
        x = q.popleft()

        if x:
            print(x.val,end=" ")
            if x.left:
                q.append(x.left)
            if x.right:
                q.append(x.right)
            
             
        else:
            print("X",end=" ")
            if q:
                q.append(None)
            
          
   


def main():
    arr =  [1,2,3,4,5,None,8,None,None,None,None,6,7]
    root = constructTreeLevelOrder(arr,0,len(arr))
    print_tree(root)
    #maxWidth(root)
   
if __name__=="__main__":
    main()
