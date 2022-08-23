from collections import deque


class Node:
    def __init__(self,data=0,left=None,right=None):
        self.data = data 
        self.left = left 
        self.right= right 

def postOrder(root):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        print(root.data,end=" ")

def level_order(root):
    print("\n Level order:")
    level=0
    q = deque([None,root])
    while q:
        node = q.pop()
        if node:
            print(node.data,end=' ')
            if node.left:
                q.appendleft(node.left)
            if node.right:
                q.appendleft(node.right)
        else:
            print(f'\nLevel {level} completed')
            level+=1 
            if q:
                q.appendleft(None)
'''
All are DFS
NLR - pre
LNR - Inorder
LRN - Postorder 

for BFS
Level order
'''

def main():
    root = Node(1,Node(2,Node(6)),Node(3,Node(4,right=Node(7)),Node(5)))
    #postOrder(root)
    level_order(root)

    
if __name__ == '__main__':
    main() 