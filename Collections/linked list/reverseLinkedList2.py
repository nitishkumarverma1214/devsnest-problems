class Node:
    
    def __init__(self,data=0,next=None):
        self.data =data
        self.next = next
    
    def __str__(self):
        return f"Node {self.data} -->{self.next}"

def cut(head,left,right):
    l1 =Node(123)
    l1.next = head
    
    for i in range(1,left):
        l1 = l1.next
    
    p2 =l2 = l1.next
    l1.next = None
    
    for i in range(left,right):
        p2 = p2.next
    
    l3 = p2.next
    p2.next = None 
    
    return l2,l3
    
def join(l1 ,l2 ,l3):
    
    head = l1
    
    while l1.next:
        l1 = l1.next
    
    l1.next = l2
    
    while l1.next:
        l1 = l1.next 
    
    
    l1.next = l3 
    
    return head
    
    
    
    
    
def reverse(head):
    if not head or not head.next:
        return head 
    p,c,n = head,head.next,head.next.next
    while n:
        c.next = p
        p,c,n = c,n,n.next
    head.next =None
    c.next =p
    return c


def solve(head,left,right):
    
    if not head.next:
        return head 
        
    l1 = head
    l2,l3 = cut(head,left,right)

    # the left boundary
    if l1 ==l2:
    
        l2 = reverse(l2)
        return join(l1 = l2,l2 = l3, l3 = None)
    # the right boundary
    l2 = reverse(l2)
    return join(l1,l2,l3)
  

if __name__ == '__main__':
    
    l1 = Node(1,Node(2,Node(3,Node(4))))
    
    print(l1)
    
    print(solve(l1,1,4))
   
    
    
    
    