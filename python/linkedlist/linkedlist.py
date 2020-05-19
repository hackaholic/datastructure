class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


class LinkedList:
    def __init__(self, node=None):
        self.head, self.tail = None, None
        self.n = -1
        if node:
            self.head, self.tail = node, node
            self.n += 1

    def insert(self, node, pos=None):
        if pos:
            print("hello")

        else:
            if self.n == -1:
                self.head, self.tail = node, node
            else:
                self.tail.next = node
                self.tail  = node
        self.n += 1

    def display(self):
        if self.head:
            temp = self.head
            while(temp):
                print(temp.value)
                temp = temp.next
        else:
            print("Empty list")

    def element_count(self):
        print("Total element: " + str(self.n + 1))

    def delete_on_pos(self, i):
        cur = self.head
        if i>=0 and i<=self.n:
            if i == 0:
                self.head = self.head.next
            else:
                pre = cur
                cur = cur.next
                nex = cur.next
                k = 1
                while(nex):
                    if i == k:
                        pre.next = cur.next
                        cur = None
                        break
                    else:
                        pre = cur
                        cur = cur.next
                        nex = cur.next
                    k +=1
            self.n -= 1      
                
        else:
            print("Please provide valid position")
            i = int(input("Position: "))
            self.delete(i)

    def delete_on_value(self, k):
        if self.head.value == k:
            self.head = self.head.next
        else:
            cur = self.head.next
            pre, nex = self.head, cur.next
            while cur:
                if cur.value == k:
                    pre.next = cur.next
                    cur = None
                    self.n -= 1
                    break
                pre = cur
                cur = nex
                nex = nex.next


    def reverse(self):
        cur = self.head
        pre, nex = None, None
        while cur:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        self.head = pre

    def deleteList(self):
        if self.head:
            cur = self.head
            while(cur):
                temp = cur
                cur = cur.next
                del temp.value
                temp.next = None
            self.head = None
        else:
            print("empty List")

def main():
    intro = """
    1 -> insert node
    2 -> list elements
    3 -> No of nodes
    4 -> search an element
    5 -> Delete a Node at position
    6 -> Delete a node on value
    7 -> Reverse the linked list
    8 -> Delete linkedlist
    99 - >  Quit"""
    obj = LinkedList()
    while True:
        print(intro)
        try:
            n = int(input("Enter choice: "))
            if n == 99:
                break
            if n == 1:
                data = int(input("Enter an element: "))
                node = Node(data)
                obj.insert(node)
            if n == 2:
                obj.display()
            if n == 3:
                obj.element_count()
            if n == 5:
                i = int(input("Provide position: "))
                obj.delete_on_pos(i)
            if n == 6:
                print("Elements: ")
                obj.display()
                i = int(input("Provide value to be deleted: "))
                obj.delete_on_value(i)
            if n == 7:
                obj.reverse()
            if n == 8:
                obj.deleteList()
                
        except Exception as e:
            print("Input should be from listed options", e)

main()
