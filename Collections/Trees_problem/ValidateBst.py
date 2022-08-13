from array_to_levelorderTree import createTree
from Tree import print_tree

prev = None
def isBST(root,isbst=True):
    if root:
        isbst = isBST(root.left,isbst)
        if not isbst:
            return isbst 
        global prev
        if root.val<=prev:
            return False 
        prev = root.val
        isbst = isBST(root.right,isbst)
        return isbst
    return isbst

def solve(root):
    global prev 
    prev = -float('inf')
    return 1 if isBST(root) else 0


def main():
    arr = [2,1,3,4]
    root = createTree(arr,None)
    print_tree(root)
    print(solve(root))
    
if __name__=="__main__":
    main()
