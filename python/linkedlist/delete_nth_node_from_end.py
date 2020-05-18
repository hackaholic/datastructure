"""
    Take two pointers, first will point to the head of the linked list and second will point to the Nth node from the beginning.
    Now keep increment both the pointers by one at the same time until second is pointing to the last node of the linked list.
    After the operations from the previous step, first pointer should be pointing to the Nth node from the end by now. So, delete the node first pointer is pointing to.
"""

import sys

class Node:
    def __init__(self, data):
        self.value = data
        self.next = None

try:
    f = open(sys.argv[1])
except Exception as e:
    print(e)
    sys.exit(0)

for i,line in enumerate(f):
    node = Node(int(line.strip("\n")))
    if i == 0:
        head = node
        cur = head
    else:
        cur.next = node
        cur = node

def display(head):
    cur = head
    while cur:
        print(cur.value)
        cur = cur.next
    print()

display(head)

def delete_from_end(head, n):
    first, second = head, head
    for i in range(n):
        if second:
            second = second.next
        else:
            break
    if i == n-1:
        if second == None:
            temp, head = head, head.next
            temp = None
        else:
            while(second.next):
                first = first.next
                second = second.next
            first.next = first.next.next
    display(head)

delete_from_end(head, 9)

