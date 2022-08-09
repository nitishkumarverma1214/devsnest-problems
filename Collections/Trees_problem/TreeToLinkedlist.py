from Tree import TreeNode,print_tree
from array_to_levelorderTree import createTree


def flatten(root):
    if root:
        ls,le = flatten(root.left)
        rs,re = flatten(root.right)

        if not root.left and not root.right:
            return root,root 
        
        if not root.left:
            root.right = rs 
            return root,re
        elif not root.right:
            root.left = None 
            root.right = ls 
            return root,le 
        else:
            root.left = None 
            root.right = ls 
            le.right = rs 
            return root,re 

    return None,None 



def main():
    arr = [1, 2, 5, 3 ,4 ,None, 6]
    root = createTree(arr,None)
    print_tree(root)
    root = flatten(root)[0]
    print_tree(root)
if __name__=="__main__":
    main()