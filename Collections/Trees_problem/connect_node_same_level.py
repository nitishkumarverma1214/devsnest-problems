from Tree import print_tree
from array_to_levelorderTree import constructTreeLevelOrder
from collections import deque
def connect_node_same_level(root):
    q = deque([None,root])
    
    prev =None
    while q:
        x = q.pop()
        if x:
            if prev:
                prev.nextRight = x 
                
            prev = x
            if x.left: 
                q.appendleft(x.left)
            if x.right:
                q.appendleft(x.right)
        else:
            
            prev = None
            
            if q:
                q.appendleft(None)

    return root 
    
if __name__=="__main__":
    arr = [10,3,5,4,1,None,2]
    root = constructTreeLevelOrder(arr,0,len(arr))
    print_tree(root)
    #print(connect_node_same_level(root))
