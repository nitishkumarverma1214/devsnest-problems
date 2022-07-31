from collections import deque
class TreeNode:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left 
        self.right = right 
  
def symmetricTree(p,q):
    if( p and not q) or (not p and q):
            return False
    if not p and not q:
        return True
    if p.val != q.val:
        return False

    return symmetricTree(p.left,q.right) and symmetricTree(p.right,q.left) 


def solve(root):
    return 1 if symmetricTree(root.left,root.right) else 0

def levelOrder(root):
    if root:
        q = deque([root])
        while q:
            x = q.pop()
            print(x.val,end=" ")
            if x.left:
                q.appendleft(x.left)
            if x.right:
                q.appendleft(x.right)

if __name__ =="__main__":
    root = TreeNode(1,TreeNode(2,TreeNode(3),TreeNode(4)),TreeNode(2,TreeNode(4),TreeNode(3)))
    levelOrder(root)
    print("---")
    print(solve(root))