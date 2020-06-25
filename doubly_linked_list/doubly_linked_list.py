# """Implement a doubly linked list data structure"""

# class ListNode:
#     """Each ListNode holds a reference to its previous node
#     as well as its next node in the List."""

#     def __init__(self, value, prev=None, next=None):
#         self.value = value
#         self.prev = prev
#         self.next = next

#     def __str__(self):
#         return f"value: {self.value}"

#     def insert_after(self, value):
#         """Wrap the given value in a ListNode and insert it
#         after this node. Note that this node could already
#         have a next node it is point to."""
#         current_next = self.next
#         self.next = ListNode(value, self, current_next)
#         if current_next:
#             current_next.prev = self.next

#     def insert_before(self, value):
#         """Wrap the given value in a ListNode and insert it
#         before this node. Note that this node could already
#         have a previous node it is point to."""
#         current_prev = self.prev
#         self.prev = ListNode(value, current_prev, self)
#         if current_prev:
#             current_prev.next = self.prev

#     def delete(self):
#         """Rearranges this ListNode's previous and next pointers
#         accordingly, effectively deleting this ListNode."""
#         if self.prev:
#             self.prev.next = self.next
#         if self.next:
#             self.next.prev = self.prev

# class DoublyLinkedList:
#     """Our doubly-linked list class. It holds references to
#     the list's head and tail nodes."""

#     def __init__(self, node=None):
#         self.head = node
#         self.tail = node
#         self.length = 1 if node is not None else 0

#     def __str__(self):
#         return f"head: {self.head}, tail: {self.tail}, length: {self.length}"

#     def __len__(self):
#         return self.length

#     def __str__(self):
#         if self.head is None and self.tail is None:
#             return "empty"

#         curr_node = self.head

#         output = ''
#         output += f'( {curr_node.value} ) <-> '

#         while curr_node.next is not None:
#             curr_node = curr_node.next
#             output += f'( {curr_node.value} ) <-> '

#         return output

#     def add_to_head(self, value):
#         """Wraps the given value in a ListNode and inserts it
#         as the new head of the list. Don't forget to handle
#         the old head node's previous pointer accordingly."""

#         # instantiate new node
#         new_head = ListNode(value)

#         # grab prev head
#         old_head = self.head

#         # increment length
#         self.length += 1

#         # if list is empty
#         if self.head is None and self.tail is None:
#             # set head to new_head
#             self.head = new_head
#             # set tail to new_head
#             self.tail = new_head
#         else:
#             # new_node's next node is the old head
#             new_head.next = old_head
#             # old_head's prev node is the new_head
#             old_head.prev = new_head
#             # set head to new_head
#             self.head = new_head

#     def remove_from_head(self):
#         """Removes the List's current head node, making the
#         current head's next node the new head of the List.
#         Returns the value of the removed Node."""

#         # if list is empty
#         if self.head is None and self.tail is None:
#             return

#         # grab the head's value
#         value = self.head.value

#         # handle 1 node in list
#         if self.head == self.tail:
#             # set head and tail to None, back to 0 nodes
#             self.head = None
#             self.tail = None
#             self.length -= 1
#         # there are multiple ListNodes
#         else:
#             # next_head will be current head's next node
#             next_head = self.head.next
#             # set next_head.prev to None
#             # erasing the ref to node to be removed
#             next_head.prev = None
#             # erase current head's next node
#             self.head.next = None
#             # set next head as the new head
#             self.head = next_head
#             # decrement length
#             self.length -= 1

#         return value

#     def add_to_tail(self, value):
#         """Wraps the given value in a ListNode and inserts it
#         as the new tail of the list. Don't forget to handle
#         the old tail node's next pointer accordingly."""

#         # instantiate new node
#         new_tail = ListNode(value)

#         # grab prev tail
#         curr_tail = self.tail

#         # increment length
#         self.length += 1

#         # if list is empty
#         if self.head is None and self.tail is None:
#             # set head to new_head
#             self.tail = new_tail
#             # set tail to new_head
#             self.head = new_tail
#         else:
#             # new_tail's prev node is the old tail
#             new_tail.prev = curr_tail
#             # curr_tail's next node is the new_tail
#             curr_tail.next = new_tail
#             # set tail to new_tail
#             self.tail = new_tail

#     def remove_from_tail(self):
#         """Removes the List's current tail node, making the
#         current tail's previous node the new tail of the List.
#         Returns the value of the removed Node."""

#         # if list is empty
#         if self.head is None and self.tail is None:
#             return

#         # grab the tail's value
#         value = self.tail.value

#         # handle 1 node in list
#         if self.head == self.tail:
#             # set head and tail to None, back to 0 nodes
#             self.head = None
#             self.tail = None
#             self.length -= 1
#         # there are multiple ListNodes
#         else:
#             # next_tail will be current tail's prev node
#             next_tail = self.tail.prev
#             # set next_tail.next to None
#             # erasing the ref to node to be removed
#             next_tail.next = None
#             # erase current tail's prev node
#             self.tail.prev = None
#             # set next tail as the new tail
#             self.tail = next_tail
#             # decrement length
#             self.length -= 1

#         return value

#     def move_to_front(self, node):
#         """Removes the input node from its current spot in the
#         List and inserts it as the new head node of the List."""
#         # handle if list is empty
#         if self.head is None and self.tail is None:
#             return

#         # handle if node is already at the front
#         if node is self.head:
#             return

#         # grab the value from node
#         value = node.value

#         # delete references
#         # decrements length
#         self.delete(node)

#         # reinsert at the head
#         # this will increment length back up
#         self.add_to_head(value)

#     def move_to_end(self, node):
#         """Removes the input node from its current spot in the
#         List and inserts it as the new tail node of the List."""
#         # handle if list is empty
#         if self.head is None and self.tail is None:
#             return

#         # handle if node is already at end
#         if node is self.tail:
#             return

#         # grab the value from node
#         value = node.value

#         # delete node's refs
#         # decrements length
#         self.delete(node)

#         # reinsert at the tail
#         # this will increment the length back up
#         self.add_to_tail(value)

#     def delete(self, node):
#         """Removes a node from the list and handles cases where
#         the node was the head or the tail"""

#         # no values in list
#         if self.head is None and self.tail is None:
#             return

#         # if node is the head
#         if node == self.head:
#             # this will remove from head
#             # and decrement length
#             self.remove_from_head()
#             return

#         # if node is the tail
#         if node == self.tail:
#             # this will remove from tail
#             # and decrement length
#             self.remove_from_tail()
#             return

#         node.delete()
#         self.length -= 1
#         return

#     def get_max(self):
#         """Returns the highest value currently in the list"""
#         curr_max = self.head.value
#         curr_node = self.head

#         while curr_node.next is not None:
#             curr_node = curr_node.next

#             if curr_node.value > curr_max:
#                 curr_max = curr_node.value

#         return curr_max

# x = DoublyLinkedList()
# x.add_to_head(12)
# x.remove_from_head()
# x.add_to_head(9)
# x.add_to_head(19)
# x.add_to_tail(24)
# x.add_to_tail(27)
# x.add_to_tail(21)
# x.move_to_front(ListNode(8,9,10))
# x.remove_from_tail()
# print(x)

#LECTURE

"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""

class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next
    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next
    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev
    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            next_node = self.next
            next_node.prev = self.prev
"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""

class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        
        # if list is currently empty
        if self.head is None and self.tail is None:
            # set the head and tail to equal the new node
            self.head = new_node
            self.tail = new_node
        else:
            # the list already has elements in it
            # make new node's next value point to current head 
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.head is None:
            return None
        head_value = self.head.value
        self.delete(self.head)
        return head_value

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value, None, None)
        self.length += 1
        if not self.tail and not self.head:
            self.tail = new_node
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        if self.tail is None:
            return None
        tail_value = self.tail.value
        self.delete(self.tail)
        return tail_value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        if node is self.head:
            return
        old_value = node.value
        self.delete(node)
        self.add_to_head(old_value)

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        if node is self.tail:
            return
        old_value = node.value
        self.delete(node)
        self.add_to_tail(old_value)

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        # the list is empty -> do nothing
        if self.head is None and self.tail is None:
            return
        # the list is only one node 
        self.length -= 1
        if self.head == self.tail:
            self.head = None                
            self.tail = None
        # the node is the HEAD node (so make sure we handle the head pointer correctly)
        elif self.head == node:
            self.head = node.next        
            node.delete()
        # the node is the TAIL node (make sure tail is handled correctly)
        elif self.tail == node:
            self.tail = node.prev        
            node.delete()
        # the node is just some node in the list
        else:
            node.delete()
            
    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head:
            return None
        max_val = self.head.value
        current = self.head
        while current:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val