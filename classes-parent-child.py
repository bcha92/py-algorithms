# Shape Class
class Shape:
    def what_am_i(self):
        print("I am a shape.")

# Rectangle Class
class Rectangle(Shape):
    # Initialization Values
    def __init__(self, l, w):
        self.length = l
        self.width = w
    # Method to Calculate Perimeter
    def perimeter(self):
        return (self.length + self.width) * 2

# Square Class
class Square(Shape):
    # Initialization Values
    def __init__(self, s):
        self.side = s
    # Method to Calculate Perimeter
    def perimeter(self):
        return self.side * 4
    def change_size(self, new):
        self.side += new

# Calling the classes Square and Rectangle
square = Square(20)
print("Length of {} by Width of {} returns the perimeter of the Square as {}."
      .format(square.side, square.side, square.perimeter()))

rectangle = Rectangle(13, 27)
print("Length of {} by Width of {} returns the perimeter of the Rectangle as {}."
      .format(rectangle.length, rectangle.width, rectangle.perimeter()))

square.change_size(4)
print("Length of {} by Width of {} returns the perimeter of the Square as {}."
      .format(square.side, square.side, square.perimeter()))

square.what_am_i()
rectangle.what_am_i()
