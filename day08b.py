# read in grid
with open('input.txt') as reader:
    lines = reader.readlines()
lines = list(map(lambda l: l.strip(), lines))

rows = len(lines)
cols = len(lines[0])
print("rows", rows, "cols", cols)

highest_scenic_score = 0

# check in 4 directions using 'for' loops
def get_scenic_score(row: int, col: int) -> int:
    global lines
    tree_height = int(lines[row][col])
    print(f"({row}, {col}) height {tree_height}", end=" ")
    trees_visible_north = 0
    trees_visible_south = 0
    trees_visible_east = 0
    trees_visible_west = 0
    # go north
    for r in range(row-1, -1, -1):
        trees_visible_north += 1
        if int(lines[r][col]) >= tree_height:
            break
    # go south
    for r in range(row+1, rows):
        trees_visible_south += 1
        if int(lines[r][col]) >= tree_height:
            break
    # go west
    for c in range(col-1, -1, -1):
        trees_visible_west += 1
        if int(lines[row][c]) >= tree_height:
            break
    # go east
    for c in range(col+1, cols):
        trees_visible_east += 1
        if int(lines[row][c]) >= tree_height:
            break
    
    scenic_score = trees_visible_north * trees_visible_south * \
        trees_visible_east * trees_visible_west
    print("scenic_score", scenic_score)
    return scenic_score

# iterate grid
for c in range(1, cols-1):
    for r in range(1, rows-1):
        scenic_score = get_scenic_score(r, c)
        highest_scenic_score = max(highest_scenic_score, scenic_score)

print(highest_scenic_score)