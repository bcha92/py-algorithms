# Dictionary of Birthday Values

# Default sample dictionary variable for names and birthdays
birthdays = {"Alice": "Apr 1", "Bob": "Dec 12", "Carol": "Mar 4"}

while True:
    print("Enter a name: (blank to quit)")
    name = input()
    # Entering blank answer results in program termination
    if name == "":
        break;
    if name in birthdays:
        print(birthdays[name] + " is the birthday of " + name)
    else:
        print("I do not have birthday information for " + name)
        print("What is their birthday: (blank to quit)")
        bday = input()
        # Entering blank answer results in program termination
        if bday == "":
            break;
        birthdays[name] = bday
        print("Birthday database updated.")
