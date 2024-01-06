from collections import deque

class Stack:
    """ Stack is implemented through deque from collections modeule.
     Deque is preferred over a list in the cases where we need quicker
       append and pop operations from both the ends of the container, 
       as deque provides an O(1) time complexity for append and pop operations
         as compared to a list that provides O(n) time complexity. """
    
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
        if len(self.stack):
            for i in self.stack:
                print(i, end = " ")
                print()
        else:
            print("Stack is empty!")

if __name__== "__main__":
    my_stack = Stack(6)
    my_stack.print_stack()
    my_stack.push(1)
    my_stack.pop()
    my_stack.print_stack()

