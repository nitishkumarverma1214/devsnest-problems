from platform import node


class Node:
  def  __init__(self,value):
    self.value = value
    self.left = None
    self.right = None
    


class binaryTree:
    def __init__(self,node):
        self.root = node
        
    def insertNode(self,root,value):
        if  root ==None:
            return  Node(value)
        
        if root.left ==None:
            root.left = self.insertNode(root.left,value)
       
        elif root.right ==None:
            root.right = self.insertNode(root.right,value)
                
    def preorder(self,root):
        if root!=None:
            print(root.value)
            self.preorder(root.left)
            self.preorder(root.right)


if __name__ =="__main__":
    tree = binaryTree(Node(1))
    tree.insertNode(tree.root,2)
    tree.insertNode(tree.root,3)
    tree.insertNode(tree.root,4)
    tree.insertNode(tree.root,5)

    tree.preorder(tree.root)


