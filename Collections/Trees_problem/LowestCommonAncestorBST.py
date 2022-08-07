# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x,left=None,right=None):
        self.val = x
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def f(root,p,q):
            if root:
                if p.val<=root.val<=q.val:
                    return root 
                if root.val >q:
                    return f(root.left,p,q)
                else:
                    return f(root.right,p,q)

        return f(root,min(p,q,key= lambda x:x.val),max(p,q,key= lambda x:x.val))

def main():
    k=1
    root =TreeNode(3,TreeNode(1,right=TreeNode(2)),TreeNode(4))
    res = Solution().lowestCommonAncestor(root,TreeNode(2),TreeNode(4))
    print(res.val)
if __name__=="__main__":
    main()
                    
        
        