class Node:
    
    def __init__(self,data=0,next=None):
        self.data =data
        self.next = next
    
    def __str__(self):
        return f"Node {self.data} -->{self.next}"



def removeNthFromEnd(head,k):
    ptr = head

    for i in range(k):
        ptr = ptr.next
    
    ptr2 = head
    

    while ptr.next:
        ptr2 = ptr2.next
        ptr = ptr.next
    

    ptr2.next = ptr2.next.next
    return head
    #print(ptr2.data)

def solve(head, k):
    
    return removeNthFromEnd(head,k)

if __name__ == '__main__':

    head =ptr =Node(0)

    for i in range(1,5):
        ptr.next =Node(i)
        ptr = ptr.next

    print(head.next)
    k=2
    print(solve(head.next,k))