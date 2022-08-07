from Tree import TreeNode,print_tree
from array_to_levelorderTree import createTree



def solve(root,s=0):
    if root and root.val !='X':
        s=solve(root.right,s)
        
        root.val = root.val + s 
        s = root.val 
        s=solve(root.left,s)
    return s
        


def main():
    arr = [4, 1, 6, 0, 2 ,5 ,7, None, None, None, 3 ,None, None ,None ,8]
    root = createTree(arr,None)
    print_tree(root)
    solve(root)
    print_tree(root)
if __name__=="__main__":
    main()