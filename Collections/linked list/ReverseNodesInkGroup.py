
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __str__(self):
        return "Node:"+str(self.val)+'-->'+str(self.next)

def reverseList(root,k):
    prev = ListNode()
    prev.next = root 
    ptr = prev
    cur = ptr.next 
    while k:
        x =cur.next
        cur.next = ptr 
        ptr = cur 
        cur = x 
        k-=1 
        
    prev.next.next = None 
    return ptr ,x 
def reverseKGroup( head, k: int) :
    ptr = head 
    nodes = 0
    while (ptr):
        nodes+=1
        ptr=ptr.next 
    loop_pass = nodes//k 
    ptr=newHead = ListNode()
    remaining = None 
    start = head
    while loop_pass:
        loop_pass-=1
        ptr.next,remaining =  reverseList(start,k)
        ptr = start 
        start = remaining
    if remaining:
        ptr.next = remaining
    return newHead.next   
def main():
    root = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5)))))
    print(root)
    k=2
    print(reverseKGroup(root,k))
if __name__ == '__main__':
    main()