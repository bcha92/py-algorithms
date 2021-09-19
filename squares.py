# New Square Class
class Square:
    # List "squares" created to store values
    squares = []
    def __init__(self, s):
        self.side = s
        # Appends the "s" input twice in "squares" list
        self.squares.append((self.side))

# Example Input Values
s1 = Square(3)
s2 = Square(11)
s3 = Square(33)
# Prints the list in the Square class
print(Square.squares)
print("")

# Prints each value in the Square class list
# four times for each side of square
for s in Square.squares:
    print("This square's sides are {} by {} by {} by {}.".format(s, s, s, s))

# Checking if a function passed twice, with same parameters
# each time will return "True" or "False" if compared.
class Person:
    def __init__(self):
        self.name = "John Doe"
        self.age = "unknown"

# Person() is called without passing variables
one_john = Person()
same_john = one_john
# This statement should return "True" because same_john is called from
# the same function as one_john by inheriting one_john values.
print(same_john is one_john)

# Another Person() is called without passing variables
two_john = Person()
# This statement should return "False" because even though one_john
# and two_john is both called from Person(), it is called two times,
# into two different variables, despite same values being passed.
print(two_john is one_john)
