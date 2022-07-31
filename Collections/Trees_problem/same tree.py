class TreeNode:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left 
        self.right = right 
  
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if( p and not q) or (not p and q):
            return False
        if not(p and q):
            return True
        if p.val != q.val:
            return False

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right) 

if __name__ =="__main__":
    p = TreeNode(None)
    q = TreeNode(1)

    print(Solution().isSameTree(p=p,q=q))