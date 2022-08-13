class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def __init__(self):
        self.count=0
        self.ans =None
    
    def kthSmallest(self, root: TreeNode, k: int) -> int:
       
        def f(root,k):
            if root:
                    f(root.left,k)
                    self.count+=1
                    if self.count==k:
                        self.ans = root.val 
                    
                    if self.count<k:
                        f(root.right,)
        f(root,k)
        return self.ans

def main():
    k=1
    root =TreeNode(3,TreeNode(1,right=TreeNode(2)),TreeNode(4))
    res = Solution().kthSmallest(root,k)
    print(res)
if __name__=="__main__":
    main()
                    
        