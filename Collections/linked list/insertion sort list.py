class Node:
    
    def __init__(self,data=0,next=None):
        self.data =data
        self.next = next
    
    def __str__(self):
        return f"Node {self.data} -->{self.next}"

def solve(head):
    # CODE HERE
    if not head or not head.next:
        return head
    prev = Node(1000)
    prev.next = head 

    ptr1 = head.next
    head.next = None
    head = prev 

    while ptr1:
        x = ptr1.next
        pt2 = head.next 
        prev = head  

        while pt2 and pt2.data<ptr1.data:
            prev = prev.next
            pt2 = pt2.next 

        ptr1.next = pt2 
        prev.next = ptr1 

        ptr1 =x 
    
    return head.next 

if __name__ == '__main__':
    
    l1 = Node(4,Node(2,Node(1,Node(3))))
    
    print(l1)
    
    print(solve(l1))
   