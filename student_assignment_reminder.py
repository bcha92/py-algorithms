names = input("Enter student names, seperated by commas: ").title().split(",")
# get and process input for a list of names
assignments = input("Enter the # of outstanding assignments each student has yet to complete, in order seperated by commas: ").split(",")
# get and process input for a list of the number of assignments
cur_grade = input("Enter current grade (0 to 100) of each student, in order seperated by commas: ").split(",")
# get and process input for current grades
max_grade = input("Enter the maximum potential grade if assignemnts are completed (0 to 100) of each student, in order seperated by commas: ").split(",")
# get and process input for maximum potential grades if student completes all outstanding assignment

# HINT: use .format() with this string in your for loop
message = "\n Hi {},\n\nThis is a reminder that you have {} assignments left to \
submit before you can graduate. You're current grade is {} and can increase \
to {} if you submit all assignments before the due date.\n"

# write a for loop that iterates through each set of names, assignments, and grades to print each student's message
for name, assignments, cur_grade, max_grade in zip(names, assignments, cur_grade, max_grade):
    print(message.format(str(name), int(assignments), int(cur_grade), int(max_grade)))
