from pyrsistent import v


class Node(object):

    def __init__(self,value):
        self.value=value
        self.next=None

class Linkedlist(object):
    def __init__(self,head=None) :
        self.head = head
    def append(self,new_node):
        if self.head == None:
            self.head = new_node
        else:
            cur = self.head
            while(cur.next!=None):
                cur=cur.next
            cur.next = new_node
    def printLinklist(self):
        cur = self.head
        while(cur):
            print(cur.value,end="->")
            cur=cur.next
        print("None")
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        cur = self.head
        cur_pos = 1
        while(cur):
            if cur_pos == position:
                return cur
            cur = cur.next
            cur_pos+=1
        return None
    def delete(self, value):
        """Delete the first node with a given value."""
        cur = self.head
        old = self.head
        if self.head.value == value:
            self.head = self.head.next
        while(cur):
            if cur.value == value:
                old.next = cur.next
                cur.next=None
                return
            old = cur
            cur = cur.next
        return
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        
        cur_pos =1
        cur = self.head
        old = self.head
        if position == 1:
            new_element.next = self.head
            self.head = new_element
        while(cur_pos <position):
            cur_pos +=1
            old = cur
            cur = cur.next
        new_element.next = cur
        old.next = new_element

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
myLinklist = Linkedlist(n1)
myLinklist.append(n2)
myLinklist.append(n3)

myLinklist.printLinklist()

# Test get_position
# Should print 3
print( myLinklist.head.next.next.value )
# Should also print 3
print( myLinklist.get_position(3).value)

# Test insert
myLinklist.insert(n4,3)
# Should print 4 now
print(myLinklist.get_position(3).value)

# Test delete
myLinklist.delete(1)
# Should print 2 now
print (myLinklist.get_position(1).value)
# Should print 4 now
print( myLinklist.get_position(2).value)
# Should print 3 now
print( myLinklist.get_position(10))

