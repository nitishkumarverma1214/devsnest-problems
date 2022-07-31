class TreeNode:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left 
        self.right = right 
    
def printLeaf(root):
    if root :
        if not root.left and not root.right:
            print(root.val)

        printLeaf(root.left)
        printLeaf(root.right)
def sum_of_leave(root,_sum=0):
    
    if root :
        # check it is a leave node
        if not root.left and not root.right:
            _sum +=root.val
            return _sum
        # return the sum of leave nodes from left and right sub tree(as it is a inner node)
        return sum_of_leave(root.left,_sum)+sum_of_leave(root.right,_sum)
    return 0
if __name__ =="__main__":
    root = TreeNode(1,TreeNode(2),TreeNode(3,TreeNode(4),TreeNode(5)))
    printLeaf(root)
    print(sum_of_leave(root))