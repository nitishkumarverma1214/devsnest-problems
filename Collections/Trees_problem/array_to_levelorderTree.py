from Tree import TreeNode,print_tree
def constructTreeLevelOrder(arr,pos,length):
    if pos < length and arr[pos]:
        root = TreeNode(arr[pos])
        root.left = constructTreeLevelOrder(arr,2*pos+1,length)
        root.right = constructTreeLevelOrder(arr,2*pos+2,length)

        return root 

    return None 

    


        

if __name__=="__main__":
    arr = [1,2,None,3,6]
    root = constructTreeLevelOrder(arr,pos=0,length =len(arr))
    print_tree(root)
    
