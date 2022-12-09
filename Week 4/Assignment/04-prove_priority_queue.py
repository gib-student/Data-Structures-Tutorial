"""
CSE212 
(c) BYU-Idaho
04-Prove - Problem 2

It is a violation of BYU-Idaho Honor Code to post or share this code with others or 
to post it online.  Storage into a personal and private repository (e.g. private
GitHub repository, unshared Google Drive folder) is acceptable.
"""

class Priority_Queue:
    """
    This queue follows the same FIFO process except that higher priority
    nodes will be dequeued before lower priority nodes.  Nodes of the same
    priority will follow the same FIFO process.
    """

    class Node:
        """
        Each node is the queue will have both a value and a priority.
        """

        def __init__(self, value, priority):
            """
            Initialize a new node
            """
            self.value = value
            self.priority = priority

        def __str__(self):
            """
            Display a single node
            """
            return "{} (Pri:{})".format(self.value, self.priority)

    def __init__(self):
        """ 
        Initialize an empty priority queue
        """
        self.queue = []

    def enqueue(self, value, priority):
        """
        Add a new value to the queue with an associated priority.  The
        node is always added to the back of the queue irregardless of 
        the priority.
        """
        new_node = Priority_Queue.Node(value, priority)
        self.queue.append(new_node)

    def dequeue(self):
        """
        Remove the next value from the queue based on the priority.  The 
        highest priority item will be removed.  In the case of multiple
        values with the same high priority, the one closest to the front
        (in traditional FIFO order) will be removed.  Priority values are
        interpreted as higher numbers have higher priority.  For example, 
        10 is a higher priority than 5.
        """
        if len(self.queue) == 0:  # Verify the queue is not empty
            print("The queue is empty.")
            return None
        # Find the index of the item with the highest priority to remove
        high_pri_index = 0
        for index in range(0, len(self.queue)):
            # print(f"high_pri_index: {high_pri_index}")
            # print(f"priority of this index's node: {self.queue[index].priority}")
            if self.queue[index].priority > self.queue[high_pri_index].priority:
                high_pri_index = index
        # Remove and return the item with the highest priority
        value = self.queue[high_pri_index].value
        del self.queue[high_pri_index]
        return value
        
    def __len__(self):
        """
        Support the len() function
        """
        return len(self.queue)

    def __str__(self):
        """ 
        Suppport the str() function to provide a string representation of the
        priority queue.  This is useful for debugging.  If you have a 
        Priority_Queue object called pq, then you run print(pq) to see the 
        contents.
        """
        result = "["
        for node in self.queue:
            result += str(node)  # This uses the __str__ from the Node class
            result += ", "
        result += "]"
        return result

# Test Cases

# Test 1
# Scenario: The queue will have 5 nodes. The first node will have a value of 25,
# the second 20, the third 15 and so on. The priority of the first node will be
# the lowest of 1, the second 2, the third 3 and so on. This will test the 
# ability of the program to find the highest priority index and display 
# it for each item in the queue.
# Expected Result: 5, 10, 15, 20, 25
print("Test 1")
# Create priority queue
queue = Priority_Queue()
# Enqueue nodes
queue.enqueue(5, 5)
queue.enqueue(10, 4)
queue.enqueue(15, 3)
queue.enqueue(20, 2)
queue.enqueue(25, 1)
# Display the five nodes
for i in range(queue.__len__()):
    node_value = queue.dequeue()
    print(node_value)

# Defect(s) Found: 
# Instead of displaying the values, each node is represented as a '1'. 
# There might be something wrong with the display function, the enqueue
# function, or perhaps the dequeue function.
print("=================")

# Test 2
# Scenario: This scenario will test the ability of the program to 
# display the proper node when it shares the same priority as 
# other nodes.
# There will be 5 nodes, 2 with a priority of 3, 2 with a priority of 2,
# and one with a priority of 1. The two nodes with a priority of 3 will
# be adjacent to each other, while the two with a priority of 2 will
# be separated in the list by the node with a priority of 1. 
# The nodes will have the following values and priorities respectively 
# and in this order in the queue:
# (2, 3), (4, 3), (6, 2), (10, 1), (8, 2)
# Expected Result: 2, 4, 6, 8, 10
print("Test 2")
# Create priority queue
queue = Priority_Queue()
# Enqueue nodes
queue.enqueue(2, 3)
queue.enqueue(4, 3)
queue.enqueue(6, 2)
queue.enqueue(10, 1)
queue.enqueue(8, 2)
# Display the five nodes
for i in range(queue.__len__()):
    node_value = queue.dequeue()
    print(node_value)

# Defect(s) Found: 
# No defects were found! I believe that I knew what the problem was
# supposed to be for this issue; while examining the code for the 
# previous test case, I noticed that the dequeue function would
# replace the current index with another one if the priority was
# greater than or equal to the priority of the current index; 
# I changed this to be only greater than, and not equal to. This
# enables it to select the first node with a higher priority,
# and does not select a following node when it shares the same
# priority.
print("=================")

# Add more Test Cases As Needed Below