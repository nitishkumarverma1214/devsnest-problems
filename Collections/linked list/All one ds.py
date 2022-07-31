
class AllOne:

    def __init__(self):
        self.key_to_count={}
        self.count_to_key={}
        self.min_key = 9999
        self.max_key = -9999
        
    def update_count_to_key(self,key,op='dec'):
        count= self.key_to_count[key]
        if op == 'inc':
           
            if count-1:
                self.count_to_key[count-1].remove(key)
                if not self.count_to_key[count-1]:
                    del self.count_to_key[count-1]

            if count not in self.count_to_key:
                self.count_to_key[count] = set()
            
            self.count_to_key[count].add(key)

        else:
            self.count_to_key[count+1].remove(key)
            if not self.count_to_key[count+1]:
                del self.count_to_key[count+1]
            if count ==0:
                del self.key_to_count[key] 
            else:
                if count not in self.count_to_key:
                    self.count_to_key[count] = set()
            
                self.count_to_key[count].add(key)
        
        
        if count:
            if self.max_key in self.count_to_key:
                self.max_key = max(self.max_key,count)
            else:
                self.max_key = count 
            if self.min_key in self.count_to_key:
                self.min_key = min(self.min_key,count)
            else:
                self.min_key = count 
        else:
            if (self.min_key not in self.count_to_key):
                if self.max_key != -9999:
                    self.min_key = self.max_key
                else: 
                    self.min_key = 9999

            if self.max_key not in self.count_to_key:
                if self.min_key != 9999:
                    self.max_key = self.min_key
                else:
                    self.max_key = -9999


    def inc(self, key: str) -> None:
        if key in self.key_to_count:
            self.key_to_count[key]+=1
        else:
            self.key_to_count[key] =1
        
        self.update_count_to_key(key,'inc')

    def dec(self, key: str) -> None:

        self.key_to_count[key]-=1
        self.update_count_to_key(key)

    def getMaxKey(self) -> str:
        if self.max_key ==-9999:
            return ""
        
        return next(iter(self.count_to_key[self.max_key]))
        

    def getMinKey(self) -> str:
        if self.min_key == 9999:
            return ""
        
        return next(iter(self.count_to_key[self.min_key]))
        


# Your AllOne object will be instantiated and called as such:
# 
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

if __name__ =="__main__":
  operation=  ["AllOne","inc","inc","inc","inc","inc","inc","dec", "dec","getMinKey","dec","getMaxKey","getMinKey"]

  operands = [[],["a"],["b"],["b"],["c"],["c"],["c"],["b"],["b"],[],["a"],[],[]]
  
  
  for ind,op in enumerate(operation):
    if op =="AllOne":
        obj = AllOne()
        print("null",end=" ")
    elif op =='inc':
        obj.inc(operands[ind][0])
        print("null",end=" ")
    elif op == 'dec':
        obj.dec(operands[ind][0])
        print("null",end=" ")
    elif op =="getMaxKey":
        print(obj.getMaxKey(),end=" ")
    else:
        print(obj.getMinKey(),end=" ")

    
