from Tree import TreeNode,print_tree
from array_to_levelorderTree import constructTreeLevelOrder


def isBalancedBinaryTree(root,isbal=True):
    if root:
        l ,isbal = isBalancedBinaryTree(root.left,isbal)
        r ,isbal = isBalancedBinaryTree(root.right,isbal)

        if r-l not in {-1,0,1}:
            isbal = False 
        
        return max(l,r)+1,isbal
    

    return -1,isbal


def main():
    arr =  [2 ,4 ,6 ,5 ,9]
    root = constructTreeLevelOrder(arr,0,len(arr))
    print_tree(root)
    print(isBalancedBinaryTree(root))
if __name__=="__main__":
    main()
