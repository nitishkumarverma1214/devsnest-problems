from Tree import TreeNode,print_tree
from array_to_levelorderTree import constructTreeLevelOrder

def serialize(root):
        if root:
            return str(root.val)+"("+serialize(root.left)+")("+serialize(root.right)+")"
        
        return 'X'

def deserialize(data):
    data = data.split('(',1)
    if data[0] !='X':
        root = TreeNode(int(data[0]))
        data = data[1]
        c =1
        for i in range(len(data)):
            if data[i] =='(':
                c+=1
            elif data[i]==')':
                c-=1
                if c==0:
                    root.left = deserialize(data[:i])
                    root.right = deserialize(data[i+2:-1])
                    return root 
    else:
        return None


def main():
    arr =  [2 ,4 ,6 ,5 ,9]
    root = constructTreeLevelOrder(arr,0,len(arr))
    print_tree(root)
    d = serialize(root)
    print(d)
    root =deserialize(d)
    print_tree(root)
if __name__=="__main__":
    main()
