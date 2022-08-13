from Tree import TreeNode ,print_tree
from array_to_levelorderTree import createTree

class Solution:
    def InorderMorisTraversal(self,root):
        if not root:
            return 
        
        cur = root
        while cur:
            if not cur.left:
                print(cur.val,end=" ")
                cur = cur.right 
            else:
                prev = cur.left 
                while prev.right and prev.right is not cur:
                    prev = prev.right 
                if not prev.right:
                    prev.right = cur 
                    cur = cur.left 
                else:
                    prev.right = None 
                    print(cur.val,end=" ")
                    cur = cur.right 

    def PreOrderMorisTraversal(self,root):
        if not root:
            return 
        
        cur = root
        while cur:
            if not cur.left:
                print(cur.val,end=" ")
                cur = cur.right 
            else:
                prev = cur.left 
                while prev.right and prev.right is not cur:
                    prev = prev.right 
                if not prev.right:
                    print(cur.val,end=" ")
                    prev.right = cur 
                    cur = cur.left 
                else:
                    prev.right = None 
                    
                    cur = cur.right 


    def PreOrderFlatten(self,root):
            if not root:
                return 
            head=ptr = TreeNode(101) 
            cur = root
            while cur:
                if not cur.left:
                    ptr.right = cur 
                    ptr = ptr.right 

                    #print(cur.val,end=" ")
                    cur = cur.right 
                else:
                    prev = cur.left 
                    while prev.right and prev.right is not cur:
                        prev = prev.right 
                    if not prev.right:
                        ptr.right = cur 
                        ptr = ptr.right 
                        #print(cur.val,end=" ")
                        prev.right = cur 
                        cur = cur.left 
                    else:
                        prev.right = None 
                        cur = cur.right 
            return head.right

    def flatten(self, root):
        if not root:
            return 
        head=None
        cur = root
        while cur:
            if not cur.left:
                if not head:
                    head = cur 
                cur = cur.right 
            else:
                prev = cur.left 
                while prev.right and prev.right is not cur:
                    prev = prev.right 
                if not prev.right:
                    prev.right = cur 
                    cur = cur.left 
                else:
                    cur.left = None
                    cur = cur.right 
        return head 


def main():
    arr = [1 ,2 ,5 ,3 ,4, None, 6]
    root = createTree(arr,None)
    print_tree(root)
    sol = Solution()
    # sol.PreOrderMorisTraversal(root)
    # print()
    print_tree(sol.PreOrderFlatten(root))

    
    
if __name__=="__main__":
    main()