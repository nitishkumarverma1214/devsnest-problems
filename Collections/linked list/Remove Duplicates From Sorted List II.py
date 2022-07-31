class ListNode:
    
    def __init__(self,val=0,next=None):
        self.val =val
        self.next = next
    
    def __str__(self):
        return f"ListNode {self.val} -->{self.next}"
class Solution(object):
    def deleteDuplicates(self,head):
        if not head or not head.next:
            return head
        p = ListNode(0)
        p.next = head
        head = p

        l=r = head.next 

        while r:
            if l.val == r.val:
                r = r.next 
            elif l.next is r:
                p.next = l
                p = l 
                l= r 

            else:
                l =r 
        
        p.next = l if not l.next else None

        return head.next 
if __name__ == "__main__":
    l1 = ListNode(1,ListNode(2,ListNode(3,ListNode(3,ListNode(4,ListNode(4,ListNode(5)))))))

    print(Solution().deleteDuplicates(l1))