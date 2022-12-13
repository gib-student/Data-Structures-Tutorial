'''
Tutorial for Tree data structure.
'''
class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        # The root of a tree is the center of it. There will
        # be nodes to both the left and the right of a typical
        # tree. In the case where there are 2 or less nodes,
        # there will not.
        self.root = None

    '''
    Insert a node into the tree where it belongs. A tree
    is numerically ordered, so greater values go to the right
    of the root while smaller ones go to its left.
    '''
    def insert(self, data):
        # If this is the first item in the tree, it becomes the root.
        if self.root is None:
            self.root = BST.Node(data)
        else:
            # Perform recursion on an algorithm until we find where
            # the value belongs
            self._insert(data, self.root)  # Start at the root

    '''
    Called by the "insert" function to find where a value belongs.
    '''
    def _insert(self, data, node):
        if data == node.data:
            return
        elif data < node.data:
            # The data belongs on the left side.
            if node.left is None:
                # We found an empty spot
                node.left = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the left sub-tree.
                self._insert(data, node.left)
        else:
            # The data belongs on the right side.
            if node.right is None:
                # We found an empty spot
                node.right = BST.Node(data)
            else:
                # Need to keep looking.  Call _insert
                # recursively on the right sub-tree.
                self._insert(data, node.right)
    
    def __iter__(self):
        yield from self._traverse_forward(self.root)
        
    def _traverse_forward(self, node):
        if node is not None:
            yield from self._traverse_forward(node.left) # for loop
            yield node.data # Start displaying after 
            yield from self._traverse_forward(node.right)
        
    def __reversed__(self):
        yield from self._traverse_backward(self.root)

    def _traverse_backward(self, node):
        if node is not None:
            yield from self._traverse_backward(node.right)
            yield node.data
            yield from self._traverse_backward(node.left)

    def get_height(self):
        if self.root is None:
            return 0
        else:
            return self._get_height(self.root)

    def _get_height(self, node):
        if node == None:
            # Once we hit the end, then return 0
            return 0
        else:
            # Do recursion to the left side and add count_left to the result
            count_left = 1 + self._get_height(node.left)
            # Do recursion on the right side and add count_right to the result
            count_right = 1 + self._get_height(node.right)

        return count_left if count_left >= count_right else count_right

'''
Demonstrate Tree code
'''
# Create a BST
tree = BST()
tree.insert(9)
tree.insert(4)
tree.insert(7)
print("First tree:")
for x in tree:
    print(x)

tree2 = BST()
tree2.insert(48)
tree2.insert(22)
tree2.insert(9)
tree2.insert(26)
tree2.insert(34)
tree2.insert(81)
tree2.insert(52)
tree2.insert(63)
tree2.insert(90)
print("Second tree:")
for x in tree2:
    print(x)