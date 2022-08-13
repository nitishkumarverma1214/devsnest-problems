from Tree import TreeNode
from array_to_levelorderTree import createTree
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: 'TreeNode', k: int) -> bool:
        s = set() 
        def helper(root,res=False):
            if root:
                if k-root.val in s:
                    return True 
                s.add(root.val)
                res = helper(root.left)
                if res:
                    return res 
                return helper(root.right)
            return res 
        return helper(root)
    
def main():
    arr =  [5,3,6,2,4,None,7]

    root = createTree(arr,None)
    print(Solution().findTarget(root,9))
   
if __name__=="__main__":
    main()
