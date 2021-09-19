# Reversing a String with a Stack

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items == []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        last = len(self.items) - 1
        return self.items[last]
    def size(self):
        return len(self.items)
    def reverse(self):
        reverse = ""
        for i in range(len(self.items)):
            reverse += self.items.pop()
        return reverse
    def reverse_list(self):
        reverse_list = []
        for i in range(len(self.items)):
            reverse_list.append(self.items.pop())
        return reverse_list

# Function to Reverse String

# Sample Input Value
stack = Stack()
for c in "Hello":
    stack.push(c)
    print(c)
print(stack.reverse())

whack = Stack()
for c in "Yesterday":
    whack.push(c)
    print(c)
print(whack.reverse())

numbers = Stack()
for i in range(1, 6):
    numbers.push(i)
    print(i)
print(numbers.items)
print(numbers.reverse_list())
