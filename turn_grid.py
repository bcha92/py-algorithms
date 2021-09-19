# Character Picture Grid

# Inverts grid[x][y] to grid[y:reverse][x]
def clockwise_turn(g):
    print("")
    # y-coordinates using length of row
    for y in range(len(g[0])):
        line = []
        # x-coordinates using length of column
        for x in reversed(range(len(g))):
            line.append(g[x][y])
        print("".join(line))
    print("")

# Grid
grid = [[".", ".", ".", ".", ".", "."],
        [".", "0", "0", ".", ".", "."],
        ["0", "0", "0", "0", ".", "."],
        ["0", "0", "0", "0", "0", "."],
        [".", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "."],
        ["0", "0", "0", "0", ".", "."],
        [".", "0", "0", ".", ".", "."],
        [".", ".", ".", ".", ".", "."]]

# Change Picture Grid to this:
# ..00.00..
# .0000000.
# .0000000.
# ..00000..
# ...000...
# ....0....
clockwise_turn(grid)
