class Node:
    
    def __init__(self,data=0,next=None):
        self.data =data
        self.next = next
    
    def __str__(self):
        return f"Node {self.data} -->{self.next}"


def cut(head):
    l1 = head
    l2 = head.next
    
    while l2.next and l2.next.next:
        l1 =l1.next
        l2= l2.next.next
    
    if l2.next:
        l1 = l1.next
    
    newHead = l1.next    
    l1.next = None 
    
    return newHead
    
    
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

def merge(l1,l2):
    head = l1
    while l1 and l2:
        x = l2.next 
        l2.next = l1.next 
        l1.next = l2
        l2 =  x 
        l1 = l1.next.next
    return head

def solve(head):
    
    if not head or not head.next:
        return 1
        
    l1 = head
    l2 = cut(head)
    
    l2 = reverse(l2)
    
    return merge(l1,l2)
    

if __name__ == '__main__':
    

    l1 =ptr =Node(0)

    for i in range(1,3):
        ptr.next =Node(i)
        ptr = ptr.next


    l2=p2 = Node(5)
    for i in range(6,9):
        p2.next =Node(i)
        p2 = p2.next
    
    print(l1)
    
    print(solve(l1))
    #print(l2)

    #print(merge(l1,l2))
    
    
    
    
    