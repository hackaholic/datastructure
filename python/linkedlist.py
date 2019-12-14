class Node:
    def __init__(self, data):
        self.value = data
        self.next = None


class LinkedList:
    def __init__(self, node):
        self.head, self.tail = node, node
        self.n = 1

    def insert(self, node, pos=None):
        if pos:
            print("hello")

        else:
            self.tail.next = node
            self.n += 1

    def display(self):




def main():
    intro = """
    1 -> insert node
    2 -> list elements
    3 -> No of nodes
    4 -> search an element"""
    print(intro)

main()
