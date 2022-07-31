class Node:
    
    def __init__(self,data,next=None):
        self.data =data
        self.next = next
    
    def __str__(self):
        return f"Node {self.data} -->{self.next}"

def length(head):
    ptr = head

    if not ptr:
        return -1
    return length(ptr.next) +1
   

def convert_bin_to_dec(head):
        num = 0
        while(head):
             num=(num*2)+head.data 
             head=head.next 
        return num

def printLL(head):

    while head:
        print(head.data,end="-->")

def reverse(head):
    
    if not head or not head.next:
        return head
    
    prev = head
    cur = head.next
    nptr = head.next.next
    
    while nptr: #cur!= None
        #cur.next
       cur.next = prev
       prev = cur
       cur = nptr
       nptr = nptr.next
    
    head.next = None
    cur.next = prev
      
    
    return cur  
    
if __name__ == '__main__':
    
    head = Node(1,Node(2,Node(3,Node(4))))
    
    print(head)
    #print(length(head))
    #print(convert_bin_to_dec(head))

    ref = reverse(head)
    printLL(ref)
