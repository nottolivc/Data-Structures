"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""

class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __str__(self):
        return f"{self.storage}"
        
    def __len__(self):
        return len(self.storage)

    def push(self, value):
        self.size += 1
        return self.storage.append(value)

    def pop(self):
        if len(self.storage) == 0:
            return None
        else:
            remove_node = self.storage.pop(self.size - 1)
            self.size -= 1
            return remove_node


x = Stack()

x.push(1)
x.push(2)
x.push(3)
x.push(4)
x.pop()

print(x)