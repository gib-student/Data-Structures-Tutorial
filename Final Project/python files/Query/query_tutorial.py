''' This example of a query of orders to be fulfilled. 
    When a customer places an order, an object is enqueued
    to the back of the queue. When they arrive at the front
    of the queue, their order is fulfilled.'''


''' Our queue data structure.
    The first item in the list will be in the 0th place while the last
    will be at the max index.'''
class order_queue:
    '''A queue in python is a list'''
    def __init__(self):
        self.queue = []
    
    def enqueue(self, order):
        # Place the order at the end of the list.
        self.queue.append(order)
    
    def dequeue(self):
        # Get the item in the 0th position.
        order = self.queue[0]
        # Remove the first item in the list to move the queue along
        del self.queue[0]
        return order

''' That's it! That's all there is to a queue. Everything below is just
    here to demonstrate how the queue works.'''



''' Demonstrate how the queue works by making 5 orders and enqueuing
    them in the queue, then dequeuing and displaying them'''

'''Build order data structure'''
def build_order(item, quantity, stock_id):
    order = {
        'item': item,
        'quantity': quantity,
        'stock_id': stock_id
    }
    return order

'''Add order to the queue'''
def enqueue_order(queue, order):
    queue.enqueue(order)

def display_order(order):
    print("item: " + str(order["item"]) + ", quantity: " + 
        str(order["quantity"]) + ", stock_id: " + str(order["stock_id"]))

# Main
def main():
    queue = order_queue()
    stock_ids = {
        'sunglasses': 25,
        'keychain': 39,
        'battery': 55,
        'wrench': 12,
        'screwdriver': 70
    }
    # Make 5 order examples
    o1 = build_order('sunglasses', 1, stock_ids["sunglasses"])
    o2 = build_order('battery', 10, stock_ids["battery"])
    o3 = build_order('wrench', 2, stock_ids["wrench"])
    o4 = build_order('screwdriver', 1, stock_ids["screwdriver"])
    o5 = build_order('keychain', 3, stock_ids["keychain"])

    # Add orders to queue
    enqueue_order(queue, o1)
    enqueue_order(queue, o2)
    enqueue_order(queue, o3)
    enqueue_order(queue, o4)
    enqueue_order(queue, o5)

    # Now we will display the orders as if we were fulfilling them
    for order_num in range(1, 6):
        print(f"Order {order_num}: ", end="")
        order = queue.dequeue()
        display_order(order)

# Execute tutorial
main()