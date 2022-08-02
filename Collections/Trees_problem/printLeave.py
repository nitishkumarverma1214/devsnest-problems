from Tree import TreeNode,print_tree
from array_to_levelorderTree import constructTreeLevelOrder


def printLeave(root):
    leaves = []
    def helper(root):
        if root:
            if not root.left and not root.right:
                leaves.append(root.val)
            helper(root.left)
            helper(root.right)

    helper(root)
    print(leaves)





def main():
    arr = [1,2,5,8,9,2,None,3,5,None,8,17,55,None,99,None,100,55,19]
    root = constructTreeLevelOrder(arr,0,len(arr))
    print_tree(root)
    printLeave(root)
if __name__=="__main__":
    main()
