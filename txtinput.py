# Gets input from user and outputs in console and some_file.txt

with open("some_file.txt", "w") as userin:
    userin.write(input("Enter your input: "))

with open("some_file.txt", "r") as userin:
    print(userin.read())
