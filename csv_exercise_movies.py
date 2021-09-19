# Writing into a CSV file exercise
# Example list of movies
movies = [["Top Gun", "Risky Business", "Minority Report"],
          ["Titanic", "The Revenant", "Inception"],
          ["Training Day", "Man on Fire", "Flight"]]

# Import CSV
import csv

# Open and write into csv file
with open("another_file.csv", "w", newline="") as file:
    writer = csv.writer(file, delimiter=",")
    for row in movies:
        writer.writerow(row)

# Checks in console if csv file was properly written in:
with open("another_file.csv", "r") as file:
    read = csv.reader(file, delimiter=",")
    for row in read:
        print(", ".join(row))
