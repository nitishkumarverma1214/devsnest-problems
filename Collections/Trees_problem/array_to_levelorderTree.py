from collections import deque
from Tree import TreeNode,print_tree


Q = deque()
 
# Helper function helps us in adding data
# to the tree in Level Order
def insertValue(val, root):
    
    newnode = TreeNode(val) if val!=None else TreeNode('X')
    if Q:
        temp = Q[0]
    if root == None:
        root = newnode
         
    # The left child of the current Node is
    # used if it is available.
    elif temp.left == None:
        temp.left = newnode
     
    # The right child of the current Node is used
    # if it is available. Since the left child of this
    # node has already been used, the Node is popped
    # from the queue after using its right child.
    elif temp.right == None:
        temp.right = newnode
        atemp = Q.popleft()
     
    # Whenever a new Node is added to the tree,
    # its address is pushed into the queue.
    # So that its children Nodes can be used later.
    Q.append(newnode)
    return root
 
# Function which calls add which is responsible
# for adding elements one by one
def createTree(a, root):
    for i in range(len(a)):
        root = insertValue(a[i], root)
    return root


        

if __name__=="__main__":
    arr = [1,3,2,5,None,None,9,6,None,None,None,None,None,7]
    
    root = createTree(arr,None)
    print_tree(root)
    
