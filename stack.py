from collections import deque

class Stack:
    
    def __init__(self, length = 5):
        
        self.length = length
        self.stack = deque()

    def push(self, value):
        if len(self.stack) < self.length:
            self.stack.append(value)
            print(f'{value} added to the stack.')
        else:
            print("Stack is full!")


    def pop(self):
        if len(self.stack):
            removed_item = self.stack.pop()
            print(f'{removed_item} is being removed!')
        else:
            print("Stack is Empty!")

    def print_stack(self):
        for i in self.stack:
            print(i, end = " ")


my_stack = Stack(6)
my_stack.print_stack()
my_stack.push(1)
my_stack.push(2)
my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
my_stack.push(6)
my_stack.print_stack()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.print_stack()

            
