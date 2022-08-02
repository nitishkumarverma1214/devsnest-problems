from Tree import TreeNode,print_tree
from array_to_levelorderTree import constructTreeLevelOrder


def left_view(root):
    view = {}
    def helper(root,level):
        if root:
           
            if level not in view:
                view[level] = root.val
            helper(root.left,level+1)
            helper(root.right,level+1)

    helper(root,0)
    print(view)




def main():
    arr = [1,2,5,8,9,2,None,3,5,None,8,17,55,None,99,None,100]
    root = constructTreeLevelOrder(arr,0,len(arr))
    print_tree(root)
    left_view(root)

if __name__=="__main__":
    main()
