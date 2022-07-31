class ListNode:
    
    def __init__(self,val=0,next=None):
        self.val  = val
        self.next = next
    
    def __str__(self):
        return f"ListNode {self.val} -->{self.next}"
class Solution:
    def make_ll_equal(self,l1,l2):
        p1,p2 = l1,l2
        while p1 or p2:
            if p1:
                p1 = p1.next
            else:
                node = ListNode(0)
                node.next = l1
                l1=node 

            if p2 :
                p2 = p2.next
            
            else: 
                node = ListNode(0)
                node.next = l2
                l2 = node 

        return l1,l2

    def addTwoNumbers(self,l1: ListNode, l2: ListNode)->ListNode:
        # CODE HERE
        if not l1 or not l2:
            return l2 if not l1 else l2 

        any_one = True
        p1,p2 = self.make_ll_equal(l1,l2)
        
        prev = None
        while any_one:
            any_one = False
            l1,l2 = p1,p2
            while l1:
        
                s = l1.val + l2.val
                #store the sum in l1
                l1.val = s%10
                # storing the carry in l2
                l2.val = s//10
                any_one = any_one or bool(l2.val)
                prev = l2
                l1 = l1.next
                l2 = l2.next

            prev.next = ListNode(0)
            if p2.val ==0:
                p2 = p2.next

            else:
                node = ListNode(0)
                node.next = p1
                p1 = node


        return p1

if __name__ == "__main__":
    l1 = ListNode(7,ListNode(2,ListNode(4,ListNode(3))))
    l2 = ListNode(5,ListNode(6,ListNode(4)))

    print(Solution().addTwoNumbers(l1,l2))