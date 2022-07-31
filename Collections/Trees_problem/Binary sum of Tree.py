from collections import deque
class TreeNode:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left 
        self.right = right 
def levelOrder(root):
    if root:
        q = deque([root])
        while q:
            x = q.pop()
            if x:
                print(x.val,end=" ")
                q.appendleft(x.left)
                q.appendleft(x.right)
            else:
                print("null",end=" ")
    else:
        print("null")

def binarysum(root,s=0):
    if root :
        s = s*2+root.val 
    
        if not root.left and not root.right:
            return s
        return binarysum(root.left,s)+ binarysum(root.right,s)

    return 0

def buttomUpBinarysum(root):
    if root:
        if not root.left and  not root.right :
            return root.val,0
        leftsum= rightsum=leftdept=rightdept=0
        if root.left:
            leftsum,leftdept = buttomUpBinarysum(root.left)
        if root.right:
            rightsum,rightdept = buttomUpBinarysum(root.right)
        height = max(leftdept,rightdept)+1
        cur = (2**height) * root.val
        subtree = cur+leftsum if root.left else leftsum
        subtree +=cur+rightsum if root.right else rightsum
        return subtree,height
    return 0,0



if __name__ =="__main__":
    root = TreeNode(1,TreeNode(0,TreeNode(0),TreeNode(1)),TreeNode(1,TreeNode(0),TreeNode(1)))
    levelOrder(root)
    # print(binarysum(root))
    print(buttomUpBinarysum(root))