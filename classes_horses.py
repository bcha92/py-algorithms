# Rider Class
class Rider:
    #Values of Rider
    def __init__(self, name, age, number):
        self.name = name
        self.age = age
        self.number = number
    def profile(self):
        return """
Rider's Profile
===============
Name: {}
Age: {}
Jockey Number: {}\n""".format(self.name, self.age, self.number)

# Horse Class
class Horse:
    #Values of Horse
    def __init__(self, name, breed, rider):
        self.name = name
        self.breed = breed
        self.rider = rider
    def profile(self):
        return """
Horse Profile
=============
Name: {}
Breed: {}
Rider: {}
{}""".format(self.name, self.breed, self.rider.name, self.rider.profile())

# Example Input
jockey = Rider("Johnathan", 24, 79)
steed = Horse("Secretariat", "Stallion", jockey)
print(steed.profile())
