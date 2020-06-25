"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import sys
sys.path.append('../doubly_linked_list')
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
        self.size += 1
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size

class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def push(self, value):
        self.storage.add_to_head(value)
        self.size += 1

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.remove_from_head()

    def len(self):
        return self.size

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return f"{self.value}"

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BSTNode(value)
        else:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BSTNode(value)

    # Return True if has value
    def contains(self, target):
        if self.value == target:
            return True
        if self.right is None and self.left is None:
            return False
        if self.left and target < self.value:
            return self.left.contains(target)
        if self.right and target > self.value:
            return self.right.contains(target)

    # Return maximum value in tree
    def get_max(self):
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if self.left:
            self.left.in_order_print(node)
        print(self.value)
        if self.right:
            self.right.in_order_print(node)

    # # Print the value of every node, starting with the given node, iterative
    def bft_print(self, node):
        level = Queue()
        level.enqueue(node)
        while level.len() > 0:
        # next_level = Queue()
        # while level.len() > 0:
            cur_node = level.dequeue()
            print(cur_node.value)
            if cur_node.left:
                level.enqueue(cur_node.left)
            if cur_node.right:
                level.enqueue(cur_node.right)
        # level = next_level

    # # Print the value of every node, starting with the given node,
    # # in an iterative depth first traversal
    def dft_print(self, node):
        branches = Stack()
        branches.push(node)
        while branches.len() > 0:
            cur_node = branches.pop()
            print(cur_node.value)
            if cur_node.left:
                branches.push(cur_node.left)
            if cur_node.right:
                branches.push(cur_node.right)

    # STRETCH Goals -------------------------
    # Note: Research may be required
    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        print(node.value)
        if node.left:
            self.pre_order_dft(node.left)
        if node.right:
            self.pre_order_dft(node.right)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        if node.left:
            self.post_order_dft(node.left)
        if node.right:
            self.post_order_dft(node.right)
        print(node.value)


root = BSTNode(8)
root.insert(3)
root.insert(9)
root.insert(10)
root.insert(12)
# lambda function is like ()=>
print_node = lambda x: print(x)

root.for_each(print_node)