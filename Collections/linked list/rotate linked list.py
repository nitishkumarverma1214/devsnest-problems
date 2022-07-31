class Node:
    
    def __init__(self,data=0,next=None):
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

def rotate(head,k):
    ptr = head

    for i in range(k):
        ptr = ptr.next
    
    ptr2 = head
    

    while ptr.next:
        ptr2 = ptr2.next
        ptr = ptr.next
    

    
    ptr.next = head
    newHead = ptr2.next
    ptr2.next = None
    return newHead

def solve(head, k):
    
    return rotate(head,k%length(head))

if __name__ == '__main__':

    head =ptr =Node(0)

    for i in range(1,5):
        ptr.next =Node(i)
        ptr = ptr.next

    print(head.next)
    k=3
    print(rotate(head.next,k))