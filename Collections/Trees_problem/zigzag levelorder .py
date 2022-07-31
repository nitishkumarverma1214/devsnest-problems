from collections import deque
class TreeNode:
    def __init__(self,val,left = None,right = None):
        self.val = val
        self.left = left 
        self.right = right 
def solve(root):
    q = deque([root])
    st = []
    iseven = True
    ans = []
    inner = []
    while q or st:
        
        x = q.pop() if q else st.pop()
        inner.append(x.val)
        if iseven:
            if x.left:
                st.append(x.left)
            if x.right:
                st.append(x.right)
           
        #odd level
        else:
            if x.left: 
                st.append(x.left)
                #q.appendleft(x.left)
            if x.right:
                st.append(x.right)
                #q.appendleft(x.right)

        

        if (iseven and not q)  or (not iseven and not st):
     
            ans.append(inner)
            inner = []
            iseven = not iseven
           

    return ans


if __name__ =="__main__":
    root = TreeNode(3,TreeNode(9),TreeNode(20,TreeNode(15),TreeNode(7)))
    print(solve(root))