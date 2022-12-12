'''Tutorial of Linked Lists.'''
class Linked_List:
    class Node:
        
        def __init__(self, data):
            # The value this node contains. Most important part of the node
            self.data = data
            # Pointer to the node before this one. Starts out pointing to nothing, 
            # but that will be changed later unless this node is the tail, in which
            # case it will remain 'None'
            self.next = None
            # Pointer to the node after this one. Starts out pointing to nothing, 
            # but that will be changed later unless this node is the head, in which case 
            # it will remain 'None'
            self.prev = None

    def __init__(self):
        # Create an empty linked list. An empty list has no head nor tail,
        # but as soon as an item is added these will change.
        self.head = None
        self.tail = None

    def insert_head(self, value):
        # Create a new node
        node = Linked_List.Node(value)
        # If the list is empty, this node will become the head and the tail
        if self.head is None:
            self.head = node
            self.tail = node
        # Otherwise, make the new node the head of the list and change the 'prev'
        # handle of the old head to point to the new one
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
    
    def insert_tail(self, value):
        node = Linked_List.Node(value)
        # If the list is empty, this node will become the head and the tail
        if self.head is None:
            self.head = node
            self.tail = node

        # Otherwise, make the new node the tail of the list and change the 'next'
        # handle of the old tail to point to the new one
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def remove_head(self):
        # If the list has only 1 item, there is no head nor tail to the list
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # Change the 'prev' handle of the node after the head to 'None'
        # since we are removing the head. Then change the head to the node
        # after the current head
        elif self.head is not None:
            self.head.next.prev = None
            self.head = self.head.next
    
    def remove_tail(self):
        # If there is only one item in the list, there is no head nor tail to the list
        if self.head == self.tail:
            self.head = None
            self.tail = None
        # Change the 'next' handle of the node before the tail to 'None'
        # since we are removing the tail. Then change the tail to the node
        # before the current tail
        elif self.tail is not None:
            self.tail.prev.next = None
            self.tail = self.tail.prev
    
    '''Insert a value into the list after the first instance of another value,
       or if the value doesn't exist in the list then place it at the end.'''
    def insert_after(self, value, new_value):
        curr = self.head        # Start the search at the head
        while curr is not None: # Continue looking until we reach the end
            if curr.data == value:
                if curr == self.tail:
                    # If we don't find the value we're looking for, just put 
                    # the new node at the end
                    self.insert_tail(new_value)
                else:
                    node = Linked_List.Node(new_value)
                    # There are 4 steps with inserting a value in the middle of
                    # the list.
                    # Step 1: Make the new node's 'prev' handle point to the node we 
                    # were looking for
                    node.prev = curr
                    # Step 2: Make the new node's 'next' handle point to the next 
                    # item in the list
                    node.next = curr.next  
                    # Step 3: Make the next node's 'prev' handle point to the new node
                    curr.next.prev = node
                    # Step 4: Make the 'prev' handle of the node preceding the new node
                    # point to the new node
                    curr.next = node
                return
            # If we don't find it, go to the next item in the list
            curr = curr.next
    
    '''Remove the first node in the list which contains a given value'''
    def remove(self, value):
        curr = self.head
        # Keep searching until we reach the end of the linked list
        while curr is not None:
            if curr.data == value:
                # If the node is the head, then we need to use the removeHead
                if curr == self.head:
                    self.remove_head()
                elif curr == self.tail:
                    # If the node is the tail, then we need to use removeTail
                    self.remove_tail()
                # Otherwise, then we'll need to manually remove the item
                else:
                    # Change the current's prev's 'next' handle to the current's next
                    curr.prev.next = curr.next
                    # Change the current's next's 'prev' handle to the current's prev
                    curr.next.prev = curr.prev
                return # Exit function after we have removed the node
            curr = curr.next

    '''Replace the value of the first node in the list which contains a given value'''
    def replace(self, old_value, new_value):
        # Keep searching until we reach the end of the list
        curr = self.head
        while curr is not None:
            # Whenever we reach an instance of the value then replace
            # its with the new value
            if curr.data == old_value:
                curr.data = new_value
            curr = curr.next

    """Iterate foward through the Linked List"""
    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr.data
            curr = curr.next

    
    """Create a string of the linked list for the print() function."""
    def __str__(self):
        output = "linkedlist["
        first = True
        for value in self:
            if first:
                first = False
            else:
                output += ", "
            output += str(value)
        output += "]"
        return output


'''Demonstrate the code'''
list = Linked_List()
list.insert_tail(5)
list.insert_tail(9)
list.insert_tail(12)
list.insert_tail(48)
list.insert_tail(20)
list.insert_tail(77)
print(f"Linked List: \t\t{list}")

# This should remove the value '12' in the 3rd position
list.remove(12)
print(f"'12' removed: \t\t{list}")

# Add a second '5'
list.insert_tail(5)
print(f"'5' inserted at tail: \t{list}")

# Remove first instance of 5
list.remove(5)
print(f"first '5' removed: \t{list}")