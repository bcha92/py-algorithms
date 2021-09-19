# Function to create a dictionary from filename (.txt or .svg)
def create_dict(filename):
    new_dict = {}
    with open(filename) as f:
        for line in f:
            con_key = line.split(": ")[0].lower()
            con_value = line.split(": ")[1].strip()
            new_dict[con_key] = con_value
    return new_dict

# Creates dictionary from filename and adds input option
def main():
    input_dict = create_dict('example.txt') # '' can be any file name
    full_name = input("Enter your first [space] and last name only: ") # Optional input statement to determine first letter of first name to key letter in dictionary.
    first_name = full_name.lower()[0]
    first_letter = first_name[0]

    print("Unique flower name with the first letter: {}".format(input_dict[first_letter]))

# Executes program without argument
main()
