# Queue Example: "FIFO" (First In, First Out)

class Queue:
    def __init__(self):
        self.items = []
    # Returns True if Stack has no value. False for otherwise.
    def is_empty(self):
        return self.items == []
    # Unlike stack, a queue adds items at the beginning of the queue.
    # Enqueue inserts item to the list
    def enqueue(self, item):
        self.items.insert(0, item)
    # Unlike stack, a queue removes the first item added to the list.
    # Dequeue removes first item from the list
    def dequeue(self):
        self.items.pop()
    # Returns the length of list
    def size(self):
        return len(self.items)

# Sample Value Input
queue = Queue()
# Determines if queue is empty (Returns True)
print("Is the queue empty? {}".format(queue.is_empty()))

# Adds numbers 0 to 4 (5 is excluded) using a for loop
for i in range(5):
    queue.enqueue(i)
# Prints the items in the queue
print(queue.items)
# Prints the size of the queue
print(queue.size())

# Removes and prints each item from the queue
for i in range(5):
    queue.dequeue()
    print("Removed {} from the Queue.".format(i))
# Checks if queue is empty (Returns False)
print("Is the queue empty? {}".format(queue.is_empty()))
# Prints the size of the queue
print(queue.size())
