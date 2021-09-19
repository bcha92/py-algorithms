# Introduction to CSV Files

import csv # Always import the csv module before starting

# Open another_file.csv as under "write" with 'newline=""' parameter
with open("another_file.csv", "w", newline="") as af:
    w = csv.writer(af, delimiter=",") # Establishes delimiter in w
    w.writerow(["one", "two", "three"]) # One row is established
    w.writerow(["four", "five", "six"]) #Another one is established

with open("another_file.csv", "r") as af: # This time, the csv file
    # is opened to read its contents on the console
    r = csv.reader(af, delimiter=",") # each item separated by ","
    for row in r: # put in a for loop to print each row joined by ", "
        print(", ".join(row))
