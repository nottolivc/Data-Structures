# """
# A queue is a data structure whose primary purpose is to store and
# return elements in First In First Out order. 

# 1. Implement the Queue class using an array as the underlying storage structure.
#    Make sure the Queue tests pass.
# 2. Re-implement the Queue class, this time using the linked list implementation
#    as the underlying storage structure.
#    Make sure the Queue tests pass.
# 3. What is the difference between using an array vs. a linked list when 
#    implementing a Queue? A linked list points to a specific set of nodes in memory, 
#    whereas an array is a side by side series of values stored in an object in one place in memory cached space   
# Stretch: What if you could only use instances of your Stack class to implement the Queue?
#          What would that look like? How many Stacks would you need? Try it!
# """

# # from ../linked_list.py import LinkedList 
# # queue with a simple python list, O(n) for add and O(1) for del
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = [] 

#     def enqueue(self, item):
#         self.storage.append(item)
#         self.size += 1
  
#     def dequeue(self):
#         if self.size > 0:
#             item = self.storage.pop(0)
#             self.size -= 1
#             return item
#         else:
#             return None 

#     def len(self):
#         return self.size

# Use linked list class for now, should add double linked list for runtime O(1)
# to avoid tree traversal as it is not a priority

import sys
sys.path.append('../singly_linked_list')
from singly_linked_list import LinkedList

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __str__(self):
        return f"{self.storage}"

    def __len__(self):
        return self.size

    def enqueue(self, value):
        add_node = self.storage.insert(len(self.storage), value)
        self.size += 1
        return add_node

    def dequeue(self):
        if(self.size > 0):
            remove_node = self.storage.pop(0)
            self.size -= 1
            return remove_node
        else:
            return None

x = Queue()
x.enqueue(1)
x.enqueue(2)
x.enqueue(3)
x.enqueue(4)

x.dequeue()

print(x)