from Tree import TreeNode,print_tree 
from array_to_levelorderTree import constructTreeLevelOrder

def lowestCommonAncestor( root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root:
            if root.val ==p or root.val ==q:
                return root 

            l = lowestCommonAncestor(root.left,p,q)
            r = lowestCommonAncestor(root.right,p,q)

            if l and r:
                return root 

            return l if l else r 

def main():
    arr = [3,5,1,6,2,0,8,None,None,7,4]
    p=5
    q=1
    root = constructTreeLevelOrder(arr,0,len(arr))
    res = lowestCommonAncestor(root,p,q)
    print(res.val)


if __name__=="__main__":
    main()