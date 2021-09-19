# Defined class called "Apple" with four properties as instances
class Apple:
    def __init__(self, w, c, t, a):
        self.weight = w
        self.color = c
        self.type = t
        self.attribute = a
        print("Created variables...")

    # "self" is used to define an instance variable for class "Apple"
    # Four instance variables are declared: w, c, t, r
    # Instance variables are normally defined inside of a special
    # method called "__init__" (to initialize) that Python calls when
    # you create an ojbect

# Calling the class Apple example
apple = Apple(0.1, "red", "cosmic crisp", "sweet")
print("Apple profile:\n")
print("Weight: {}kg".format(apple.weight))
print("Color: " + apple.color)
print("Type: " + apple.type)
print("Attribute: " + apple.attribute + "\n\n")


# Another class defined here as "Circle" with one method.
class Circle:
    # Initializes the value of "radius"
    def __init__(self, r):
        # Math module is imported
        import math
        self.pi = math.pi
        self.radius = r
        print("Created variables...")
    # This method calculates and returns the area of the circle
    # based on initialized values of radius and pi
    def area(self):
        return self.pi * (self.radius ** 2)

# Calling the class Circle example
circle = Circle(5)
print("**Check Value**: The value of pi is {}".format(circle.pi))
print("The radius of {} in the circle returns an area of {}.\n\n"
      .format(circle.radius, circle.area()))


# This is a class defined here as "Triangle" with one method.
class Triangle:
    # Initializes the value of "width" and "height"
    def __init__(self, w, h):
        self.width = w
        self.height = h
        print("Created variables...")
    # This method calculates and returns the area of the triangle
    def area(self):
        return (self.width * self.height) / 2

# Calling the class Triangle example
triangle = Triangle(6, 7)
print("The width of {} and height of {} in the triangle returns an area of {}.\n\n"
      .format(triangle.width, triangle.height, triangle.area()))

# This class defines "Hexagon" with one method.
class Hexagon:
    # Initializes each value of the hexagon six "sides"
    # Assigns default values if less than 6 variables given
    def __init__(self, s1, s2, s3, s4, s5, s6):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        self.s4 = s4
        self.s5 = s5
        self.s6 = s6
        print("Created variables...")
    # This method calculates and returns the perimeter of the hexagon
    def perimeter(self):
        return self.s1 + self.s2 + self.s3 + self.s4 + self.s5 + self.s6

# Calling the class Hexagon example with all six variables
hexagon = Hexagon(1, 2, 3, 4, 5, 6)
print("""The hexagon side lengths of {}, {}, {}, {}, {}, and {}
returns a perimeter of {}.\n"""
      .format(hexagon.s1, hexagon.s2, hexagon.s3, hexagon.s4, hexagon.s5,
              hexagon.s6, hexagon.perimeter()))

