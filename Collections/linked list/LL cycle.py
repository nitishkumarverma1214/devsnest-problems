class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        if not head:
            return head
        
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow:
                break
        
        if not fast or not fast.next:
            return None
        
        fast = head
        while fast :
            if fast is slow:
                return slow
            fast = fast.next
            slow = slow.next

if __name__ == '__main__':
    head = ListNode(1)
    node = ListNode(2)
    node.next = head
    head.next = node
    
    print(Solution().detectCycle(head))
            
            