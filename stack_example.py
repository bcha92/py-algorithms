# Stack Example: "LIFO" (Last In, First Out)

class Stack:
    def __init__(self):
        self.items = []
    # Returns True if Stack has no value. False for otherwise.
    def is_empty(self):
        return self.items == []
    # Adds value to end of list
    def push(self, item):
        self.items.append(item)
    # Removes value from end of list
    def pop(self):
        return self.items.pop()
    # Returns the last item on list
    def peek(self):
        last = len(self.items) - 1
        return self.items[last]
    # Returns the length of list
    def size(self):
        return len(self.items)

# Sample Value input
stack = Stack()
# Determines if stack is empty (Returns True)
print("Is the stack empty? {}".format(stack.is_empty()))

# Determines if stack is empty (Returns False)
# Value of 1 added to list
item = 1
stack.push(item)
print("Item(s) is/are added to list: {}".format(item))
print("Is the stack empty? {}".format(stack.is_empty()))

# Determines if stack is empty (Returns True)
# Prints out the value of 1 after "pop" from list
item = stack.pop()
print("Item(s) is/are removed from list: {}".format(item))
print("Is the stack empty? {}".format(stack.is_empty()))

# Inserts a list of numbers 0 to 5 (6 is excluded) using for loop
for i in range(0, 6):
    stack.push(i)
    print("Item(s) is/are added to list: {}".format(i))
# peek prints the last item inserted in stack
print("Peeking at the stack (last item added): {}".format(stack.peek()))
# size prints the length of the list
print("There are {} items in this stack.".format(stack.size()))
