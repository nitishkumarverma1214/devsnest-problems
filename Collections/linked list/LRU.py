class DoublyLL:
    
    def __init__(self,key=-1,val=-1):
        self.val = val
        self.key = key
        self.prev =self.next = None
        
def deleteNode(node):
    
    node.prev.next = node.next
    node.next.prev = node.prev
    #del node

def insert_x_left_of_y(node_x,node_y):
    node_x.next = node_y
    node_x.prev = node_y.prev
    
    node_x.prev.next = node_x
    node_y.prev = node_x
    
class LRUCache(object):
    

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.leftend , self.rightend = DoublyLL(),DoublyLL()
        self.leftend.next ,self.rightend.prev = self.rightend,self.leftend
        self.hashMap = {}
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.hashMap:
            return -1
        
        node = self.hashMap[key]
        deleteNode(node)
        insert_x_left_of_y(node,self.rightend)        
        
        
        
        return node.val

    def put(self, key, value):
        node = DoublyLL(key,value)
        if key in self.hashMap:
           deleteNode(self.hashMap[key])
           insert_x_left_of_y(node,self.rightend)
           self.hashMap[key] = node 

        else:
            insert_x_left_of_y(node,self.rightend)
            self.hashMap[key] = node
            if (len(self.hashMap)>self.capacity):
                node_to_remove = self.leftend.next
                del self.hashMap[node_to_remove.key]
                deleteNode(node_to_remove)



      
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ =="__main__":
  operation=  ["LRUCache","put","put","get","put","get","put","get","get","get"]
  operands = [[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]
  
  
  for ind,op in enumerate(operation):
    if op =="LRUCache":
        capacity = operands[ind][0]
        lru = LRUCache(capacity)
        print(lru)
    elif op =="put":
        key,val = operands[ind]
        print(lru.put(key,val),end=" ")
    elif op == "get":
        key = operands[ind][0]
        print(lru.get(key),end=" ")
