# read in grid
with open('input.txt') as reader:
    lines = reader.readlines()
lines = list(map(lambda l: l.strip(), lines))

rows = len(lines)
cols = len(lines[0])
print("rows", rows, "cols", cols)

# the entire edge of grid is visible
num_visible = (rows * 2 + cols * 2) - 4
print("edge_visible", num_visible)

# check in 4 directions using 'for' loops
def is_visible(row: int, col: int) -> int:
    global lines
    tree_height = int(lines[row][col])
    print(f"({row}, {col}) height {tree_height}")
    # go north
    for r in range(row-1, -1, -1):
        if int(lines[r][col]) >= tree_height:
            break
        if r == 0:
            return 1
    # go south
    for r in range(row+1, rows):
        if int(lines[r][col]) >= tree_height:
            break
        if r == rows-1:
            return 1
    # go west
    for c in range(col-1, -1, -1):
        if int(lines[row][c]) >= tree_height:
            break
        if c == 0:
            return 1
    # go east
    for c in range(col+1, cols):
        if int(lines[row][c]) >= tree_height:
            break
        if c == cols-1:
            return 1
    
    return 0

# iterate grid and count visible trees
for c in range(1, cols-1):
    for r in range(1, rows-1):
        num_visible += is_visible(r, c)

print(num_visible)