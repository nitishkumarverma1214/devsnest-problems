class Node:
    
    def __init__(self,data=0,next=None):
        self.data =data
        self.next = next
    
    def __str__(self):
        return f"Node {self.data} -->{self.next}"

def solve(head):
    if not head or not head.next:
        return head 

    slow = head 
    fast = head.next 
    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next
    
    return slow if not fast else slow.next 

if __name__ == '__main__':
    
    l1 = Node(1,Node(2,Node(3,Node(4))))
    
    print(l1)
    
    print(solve(l1))
   
