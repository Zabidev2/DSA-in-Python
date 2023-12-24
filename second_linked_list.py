class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self, head = None):
        self.head = None

    def add_node(self, data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            next_node = self.head
            while next_node.next != None:
                next_node = next_node.next
            next_node.next = node

    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

list = LinkedList()
list.add_node(5)
list.print_list()