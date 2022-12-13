'''Practice problem. Most of the code will be completed for you 
   except for a few small problems. In order to find them you will
   need to have an understanding of how the program works. Find
   the errors and fix them.'''

'''In this problem, there will be several different linked lists, 
   all which contain 3 elements. The linked list will be a math
   equation looking like the following: x * y^z. The first element
   in each list (the head) is x, or the coefficient. The second
   element is y, or the base, and the third element in each list
   is z, or the exponent.'''

class Equation:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self, coefficient, base, exponent):
        self.head = None
        self.tail = None
        self.insert_coefficient(coefficient)
        self.insert_base(base)
        self.insert_exponent(exponent)

    def insert_coefficient(self, value):
        self.head = value
        
    def insert_base(self, value):
        node = Equation.Node(value)
        coefficient = self.head
        node.prev = coefficient
    
    def insert_exponent(self, value):
        node = Equation.Node(value)
        coefficient = self.head
        base = coefficient.next
        base.next = node
        node.prev = base

    def replace(self, old_value, new_value):
        curr = self.head
        while curr is not None:
            if curr.data == old_value:
                curr.data = new_value
            curr = curr.next
    
    def do_math(self):
        coefficient = self.head
        base = coefficient.next
        exponent = self.tail

        return coefficient.data * (base.data ** exponent.data)

    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr.data
            curr = curr.next

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

'''Demonstrate code'''
equation1 = Equation(3, 2, 2)
result1 = equation1.do_math()

equation2 = Equation(7, 4, 5)
result2 = equation2.do_math()

equation3 = Equation(1, 3, 9)
result3 = equation3.do_math()

equation4 = Equation(4, 2, 8)
result4 = equation4.do_math()

equation5 = Equation(9, 6, 3)
result5 = equation5.do_math()

'''Results should be:
   result1: 12
   result2: 7168
   result3: 19683
   result4: 1024
   result5: 1944
   '''
print(f"result1: {result1}")
print(f"result2: {result2}")
print(f"result3: {result3}")
print(f"result4: {result4}")
print(f"result5: {result5}")