class Node:
    
    def __init__(self,data=0,next=None):
        self.data =data
        self.next = next
    
    def __str__(self):
        return f"Node {self.data} -->{self.next}"


def oddEven(head):
    if not head or not head.next or not head.next.next:
        return head
    prev = head
    ptr1 = head.next 
    ptr2 = head.next.next 
    

    while ptr1 and ptr2:
        x = ptr2.next
        ptr2.next = prev.next 
        prev.next = ptr2
        ptr1.next = x
        prev = ptr2
        ptr2 = x.next if x else None
        ptr1 = x

    return head

if __name__ == '__main__':

    head =ptr =Node(0)

    for i in range(1,6):
        ptr.next =Node(i)
        ptr = ptr.next

    print(head.next)

    print(oddEven(head.next))