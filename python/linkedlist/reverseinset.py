# LinkedList Node
class Node:
    def __init__(self, value=None):
        if value:
            self.value = value
        self.next = None

# LinkedList class:
class LinkedList:
    def __init__(self, node=None):
        self.head = node
    
    # Append new node
    def insert(self, value):
        node = Node(value)
        cur = self.head
        if cur:
            while(cur.next):
                cur = cur.next
            cur.next = node
        else:
            self.head = node

    # Display Linked List
    def display(self):
        cur = self.head
        while(cur):
            print(cur.value)
            cur = cur.next

    # Reverse Linked List in set
    def reverseinset(self, k):
        temp , tail = self.head, None
        while temp:     
            count = 1
            cur = temp
            pre, nex = None, None
            while cur and count <= k:
                nex = cur.next
                cur.next = pre
                pre = cur
                cur = nex
                count += 1
            if tail:
                tail.next = pre
            else:
                self.head = pre
            tail = temp
            temp = cur

llist = LinkedList()
llist.insert(1)
llist.insert(2)
llist.insert(3)
llist.insert(4)
llist.insert(5)
llist.insert(6)
llist.insert(7)
llist.insert(8)
llist.insert(9)
llist.insert(10)

# Display Linked List

llist.display()
k=4
llist.reverseinset(k)
llist.display()
