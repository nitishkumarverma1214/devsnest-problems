from Tree import TreeNode
from array_to_levelorderTree import createTree
from Tree import print_tree



st =[]
pos = 0
def storeInorder(root):
    if root:
        storeInorder(root.left)
        st.append(root.val)
        storeInorder(root.right) 

def fixTree(root):
    if root:
        fixTree(root.left)
        global pos
        root.val = st[pos]
        pos+=1 
        fixTree(root.right)

    
def solve(root):
    storeInorder(root)
    st.sort()
    fixTree(root)
   

    return root 


def main():
    root=TreeNode(1,TreeNode(3,left=None,right =TreeNode(2)))
    print_tree(root)
    root = solve(root)
    print_tree(root)
    
if __name__=="__main__":
    main()