f = open("some_file.txt", "r")
file_data = f.read()
print(file_data)
f.close()

g = open("some_file.txt", "w")
g.write("Hello there! New Line")
g.close()

h = open("some_file.txt", "r")
file_data = h.read()
print(file_data)
h.close()