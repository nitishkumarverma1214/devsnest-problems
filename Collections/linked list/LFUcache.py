
class DoublyLL(object):
    def __init__(self,key = -1, val=-1):
        self.key = key
        self.val = val
        self.prev = self.next = None 
        self.cnt =1
    

def insertinLL(nodex, nodey):
    nodex.next = nodey
    nodex.prev = nodey.prev
    nodex.prev.next = nodex
    nodey.prev = nodex
    
def deletefromLL(node):
    node.prev.next = node.next
    node.next.prev = node.prev
        
def updateFreqMap(freqmap,key,oldFreq,leastFreq):
    newCount = oldFreq+1
    if oldFreq:  
        del freqmap[oldFreq][key]
        if not freqmap[oldFreq]:
            del freqmap[oldFreq]
    if newCount not in freqmap:
        freqmap[newCount] = dict() 
    
    freqmap[newCount][key] = None 

    #update mincount
    if leastFreq not in freqmap:
        leastFreq = newCount
    return leastFreq
class LFUCache(object):

    def __init__(self, capacity):
        
        self.capacity = capacity
        self.hashmap={} 
        self.leftend,self.rightend = DoublyLL(),DoublyLL()
        self.freqmap = {}# key: freq and value: linked list on node
        self.leastFreq = -1
        self.leftend.next = self.rightend
        self.rightend.prev = self.leftend
       
        

    def get(self, key):
        if key not in self.hashmap:
            return -1
        node = self.hashmap[key]
        oldCount = node.cnt
        #updating the freq map
        self.leastFreq = updateFreqMap(self.freqmap,key,oldCount,self.leastFreq)
        #updating the new position in Doubly Linked List
        #removing from original position
        deletefromLL(node)
        #updating the count
        node.cnt = oldCount+1
        #inserting at end
        insertinLL(node,self.rightend)
        
        #returning the node value
        return node.val
       
        

    def put(self, key, value):
        if self.capacity ==0:
                return 
        if key in self.hashmap:
            node = self.hashmap[key]
            oldfreq = node.cnt
            self.leastFreq = updateFreqMap(self.freqmap,key,oldfreq,self.leastFreq)
            #removing the original position
            deletefromLL(node)
            #update the node value and count
            node.val = value
            node.cnt+=1
            #insert the node at the end
            insertinLL(node,self.rightend)

            # update the key with new node
            self.hashmap[key] = node 
        else:
           
            if len(self.hashmap) +1 > self.capacity:
                #select the node with least frequency 
                key_of_node = next(iter(self.freqmap[self.leastFreq]))
                del self.freqmap[self.leastFreq][key_of_node]
                if not self.freqmap[self.leastFreq]:
                    del self.freqmap[self.leastFreq]
                node_to_remove = self.hashmap[key_of_node]
                del self.hashmap[key_of_node]
                deletefromLL(node_to_remove)
                    
            #create a new node 
            newNode = DoublyLL(key,value)
            # update the new node in hashmap
            self.hashmap[key] = newNode
            #insert
            insertinLL(newNode,self.rightend)

            #update the freqMap
            self.leastFreq = 1
            self.leastFreq = updateFreqMap(self.freqmap,key,0,self.leastFreq)
      


if __name__ =="__main__":
    operation=  ["LFUCache","put","put","get","get","put","get","get","get"]
    operands= [[2],[2,1],[3,2],[3],[2],[4,3],[2],[3],[4]]
  
    for ind,op in enumerate(operation):
        if op =="LFUCache":
            capacity = operands[ind][0]
            lfu = LFUCache(capacity)
            print("null",end=" ")
        elif op =="put":
            key,val = operands[ind]
            lfu.put(key,val)
            print("null",end=" ")
        elif op == "get":
            key = operands[ind][0]
            print(lfu.get(key),end=" ")
