class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


class LinkedList:
    def __init__(self, node=None):
        self.n = -1
        if node:
            self.head, self.tail = node, node
            self.n = 0
        self.head, self.tail = None, None

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
        temp = self.head
        while(temp):
            print(temp.value)
            temp = temp.next

    def element_count(self):
        print("Total element: " + str(self.n + 1))

    def delete(self, i):
        cur = self.head
        if i>=0 and i<=self.n:
            if i == 0:
                self.head = head.next
            else:
                pre = cur
                cur = cur.next
                nex = cur.next
                k = 1
                while(nex):
                    if i == k:
                        pre.next = cur.next
                    else:
                        pre = cur
                        cur = cur.next
                        nex = cur.next
                    k +=1
                
        else:
            print("Please provide valid position")
            i = int(input("Position: "))
            self.delete(i)

def main():
    intro = """
    1 -> insert node
    2 -> list elements
    3 -> No of nodes
    4 -> search an element
    5 - > Delete an element at position
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
                obj.delete(i)
                
        except Exception as e:
            print("Input should be from listed options", e)

main()
