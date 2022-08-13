from Tree import TreeNode
from array_to_levelorderTree import createTree
from Tree import print_tree


def increasingOrderTree(val,res):
    
    newHead=dummy = TreeNode(101)

def inorder(root):
    if root:
         inorder(root.right)
         increasingOrderTree(root.val)
         inorder(root.left)
   


def main():
    arr = [5,3,6,2,4,None,8,1,None,None,None,None,None,7,9]
    root = createTree(arr,None)
    print_tree(root)
    
    
if __name__=="__main__":
    main()