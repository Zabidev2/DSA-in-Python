class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self, head = None):

        self.head = None

    
    def add_node(self,data):
        node = Node(data)
        if self.head == None:
            self.head = node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = node

    def print_linkedlist(self):
        current_node = self.head
        while current_node:
            print(f"{current_node.data}" , end="--->")
            current_node = current_node.next
        print()

    def insert_at_beginning(self,value):
        if self.head == None:
            self.head = Node(value)
            return
        else:
            current_head = self.head
            self.head = Node(value)
            self.head.next = current_head
            return

    def search(self, item):
        found = False
        if self.head == None:
            print("The Linked List is empty!")
            return
        elif self.head.data == item:
            print(f"{item} found in the linkedlist!")
            found = True
            return
        else:
            current_node = self.head
            while current_node.next:
                if current_node.data == item:
                    print(f"{item} is in the linkedlist!")
                    found = True
                    return
                current_node = current_node.next

            if current_node.data == item and self.head.data != item:
                print(f"{item} found in the linkedlist!")
                found = True      
            if not found:
                print(f"{item} not found in Linked List!")   

    def insert_values(self, list_of_items):
        self.head = None
        for value in list_of_items:
            self.add_node(value)

    def get_length(self):
        counter = 0
        current_node = self.head
        if self.head == None:
            return counter
        else:
            while current_node:
                counter = counter + 1
                current_node = current_node.next
            return counter
        
    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            print("Index is out of range!")
            return
        elif index == 0:
            self.head = self.head.next
            return
        else:
            counter = 0
            current_node = self.head
            while current_node:
                if counter == index - 1:
                    removed_node = current_node.next
                    current_node.next = removed_node.next
                    print(f"{removed_node.data} removed from the linked list!")
                    return
                counter =+ 1
                current_node = current_node.next

    def insert_at(self, index, value):
        if index == 0:
            self.insert_at_beginning(value)
            return
        elif index == self.get_length:
            self.add_node(value)
            return
        else:
            node = Node(value)
            counter = 0
            current_node = self.head
            while current_node:
                if counter == index - 1:
                    replaced_node = current_node.next
                    current_node.next = node
                    node.next = replaced_node
                    print(f"{node.data} added at position {index}")
                    return
                counter =+ 1
                current_node = current_node.next
        
    def reverse():
        pass        



linked_list = LinkedList()
#linked_list.insert_values(['Zabi', 'Zubi', '3'])
linked_list.add_node(5)
linked_list.add_node(6)
linked_list.add_node(7)
linked_list.add_node(8)
linked_list.print_linkedlist()
linked_list.insert_at_beginning(100)
linked_list.print_linkedlist()
linked_list.remove_at(2)
linked_list.print_linkedlist()
linked_list.insert_at(2,"zabi")
linked_list.print_linkedlist()






