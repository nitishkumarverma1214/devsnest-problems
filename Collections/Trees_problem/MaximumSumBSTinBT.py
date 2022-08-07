from Tree import TreeNode,print_tree
from array_to_levelorderTree import createTree

class Solution:
    def __init__(self):
        self.msum=0
        self.m=100000
        self.mini=-100000
    def maxSumBST(self, root: TreeNode) -> int:
        def f(root):
            if not root or root.val=='X':
                return self.m,self.mini,0 
            lmin,lmax,lsum = f(root.left)
            rmin,rmax,rsum = f(root.right)
            if lmax<root.val<rmin:
                self.msum = max(self.msum,lsum+rsum+root.val)
                return min(lmin,root.val),max(rmax,root.val),lsum+rsum+root.val
            else:
                return self.mini,self.m,0
        f(root)
        return self.msum


def main():
    
    arr = [1,4,3,2,4,2,5,None,None,None,None,None,None,4,6]
    root = createTree(arr,None)
    print_tree(root)
    sol = Solution()
    res = sol.maxSumBST(root)
    print(res)
if __name__=="__main__":
    main()
                    
        
        