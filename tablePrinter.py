# Table Printer
# Prints nested arrays in neat rows and columns

# Main Function for printTable()
def printTable(nest):
    # For each row within the list:
    for row in range(len(nest)):
        maxWidth = 0
        # Determines the maximum column width of each item in row
        for item in nest[row]:
            if len(item) >= maxWidth:
                maxWidth = len(item) + 1
        # Adds space to the left in each column item to max width + 1
        for cat in range(len(nest[row])):
            nest[row][cat] = nest[row][cat].rjust(maxWidth)
    # Appends items on each column to new row
    # and outputs the resulting new rows with right-alignment spacing
    for col in range(len(nest[0])):
        trow = []
        for nrow in range(len(nest)):
            trow.append(nest[nrow][col])
        print("".join(trow))

# Example Data
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
# Execution
printTable(tableData)
