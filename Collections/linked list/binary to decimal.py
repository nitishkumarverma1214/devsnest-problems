class Node:
    
    def __init__(self,data,next=None):
        self.data =data
        self.next = next
    
    def __str__(self):
        return f"Node {self.data} -->{self.next}"

def length(head):
    count =0
    ptr = head
    while(ptr):
        count+=1
        ptr =ptr.next
    return count

def convert_bin_to_dec(head):
    
    pow = length(head)-1
    decimal = 0
    ptr = head
    for i in range(pow,-1,-1):
        if ptr.data:
            decimal += 2**i 
        ptr = ptr.next
    
    return decimal

    
    
if __name__ == '__main__':
    
    head = Node(1,Node(0,Node(1)))
    
    print(head)
    
    print(convert_bin_to_dec(head))
