from Tree import TreeNode,print_tree
from array_to_levelorderTree import constructTreeLevelOrder

def pathSum(root, targetSum,cursum =0,issum=False):
    if root:
        
            if (cursum+root.val) == targetSum and not root.left and not root.right:
                issum = True
        
            issum = pathSum(root.left,targetSum,root.val+cursum,issum)
            issum = pathSum(root.right,targetSum,root.val+cursum,issum)
        
    return issum



    

def main():
    arr = [11,3,6 ,9 ,None, 9, 3, 9 ,7 ,None, None,  8]
    root = constructTreeLevelOrder(arr,0,len(arr))
    print_tree(root)
    print(pathSum(root,30))

if __name__=="__main__":
    main()
