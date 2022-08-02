from Tree import TreeNode,print_tree
from array_to_levelorderTree import constructTreeLevelOrder
def left_view(root,res):

    def helper(root):
        if root:
            if root.left or root.right:
                res.append(root.val)
            if root.left:
                helper(root.left)
            else:
                helper(root.right)

    helper(root)
    
    return res 
def printLeave(root,res):
    def helper(root):
        if root:

            #inorder leave traversal
            helper(root.left)
            if not root.left and not root.right:
                res.append(root.val)
            
            helper(root.right)

    helper(root)
    return res 
def buttom_up_right_view(root,res):
    
    def helper(root):
        if root:
            if root.right or root.left:
                if root.right:
                    helper(root.right)
                    
                else:
                    helper(root.left)
                res.append(root.val)
            
            
    helper(root)
    return res 
    
def solve(root):
    res = [root.val]
    if root.right and root.left:
        left_view(root.left,res)
        printLeave(root,res)
        buttom_up_right_view(root.right,res)
        
    return res

def main():
    arr = [3]
    root = constructTreeLevelOrder(arr,0,len(arr))
    print_tree(root)
    r = solve(root)
    print(r)

if __name__=="__main__":
    main()
