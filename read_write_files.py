# File Path

import os # Selects file for import as "os"
os.path.join("Users", "ninja", "OneDrive", "Desktop", "saved_codes",
             "py3", "some_file.txt") # File path to some_file.txt

# Writing to Files

sf = open("some_file.txt", "w") # Opens file to begin task
sf.write("Hi from Python!\n-DedPanda\n") # Task in the some_file.txt as "sf"
sf.close() # Closes file after you finish task

# Reading from Files

sr1 = open("some_file.txt", "r") # Opens file
print(sr1.read()) # Prints content of some_file.txt to console.
sr1.close() # Closes file after task finished

# Alternative method writing to files without the .close()

with open("some_file.txt", "w") as sw: # Opens file to begin task as "sw"
    sw.write("Hi again from Python!\n-DedPanda Society\n")
    # Task to some_file.txt and automatically closes the file at end of "with"

# Alternative method reading files without the .close()

with open("some_file.txt", "r") as sr2: # Opens file to begin task as "sr2"
    print(sr2.read()) # Prints content of some_file.txt to console
    # and automatically closes the file at the end of "with"

# To access and append the contents of the file to a list:

# Create a list first (if not have done already)
my_list = [] # Alternatively, typing "my_list = list()" is also perfectly
                # a preferable alternative to some
with open("some_file.txt", "r") as sr3: # Open file set to "read"
    my_list.append(sr3.read()) # Append the contents of file as string

print(my_list) # Result should be shown in my_list
