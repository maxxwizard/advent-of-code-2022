# TODO not working correctly

# read in motions
with open('input.txt') as reader:
    lines = reader.readlines()
lines = list(map(lambda l: l.strip(), lines))

# use a set to store visited coordinates
visited_set = set()
visited_set.add((0, 0))

# initialize our rope
# all "knots" start at origin
rope_length = 10
rope: list[tuple[int, int]] = list()
for i in range(rope_length):
    rope.append((0, 0))

# same coordinates or adjacent
def is_touching(src, dst) -> bool:
    if src[0] == dst[0] and src[1] == dst[1]:
        return True
    elif move(src, 'U') == dst:
        return True
    elif move(src, 'D') == dst:
        return True
    elif move(src, 'L') == dst:
        return True
    elif move(src, 'R') == dst:
        return True
    elif move(src, 'NE') == dst:
        return True
    elif move(src, 'NW') == dst:
        return True
    elif move(src, 'SE') == dst:
        return True
    elif move(src, 'SW') == dst:
        return True
    return False

def is_directly_two_steps_away(src, dst) -> bool:
    if src[0] == dst[0]:
        return (abs(src[1] - dst[1]) == 2)
    if src[1] == dst[1]:
        return (abs(src[0] - dst[0]) == 2)
    
    return False

# moves a knot 1 unit in a direction
def move(knot, direction) -> tuple[int, int]:
    match direction:
        case 'U' | 'N':
            return (knot[0]+1, knot[1])
        case 'D' | 'S':
            return (knot[0]-1, knot[1])
        case 'L' | 'W':
            return (knot[0], knot[1]-1)
        case 'R' | 'E':
            return (knot[0], knot[1]+1)
        case 'NE':
            return (knot[0]+1, knot[1]+1)
        case 'NW':
            return (knot[0]-1, knot[1]+1)
        case 'SE':
            return (knot[0]+1, knot[1]-1)
        case 'SW':
            return (knot[0]-1, knot[1]-1)
    raise ValueError()

def get_bearing(src, dst) -> str:
    if dst[0] == src[0] and dst[1] > src[1]:
        return 'N'
    if dst[0] == src[0] and dst[1] < src[1]:
        return 'S'
    if dst[1] == src[1] and dst[0] < src[0]:
        return 'W'
    if dst[1] == src[1] and dst[0] > src[0]:
        return 'E'
    if dst[0] > src[0] and dst[1] > src[1]:
        return 'NE'
    if dst[0] > src[0] and dst[1] < src[1]:
        return 'SE'
    if dst[0] < src[0] and dst[1] > src[1]:
        return 'NW'
    if dst[0] < src[0] and dst[1] < src[1]:
        return 'SW'
    print("src", src)
    print("dst", dst)
    raise ValueError()

def print_rope():
    global rope
    # assume 5 rows 6 cols
    for i in range(5):
        for j in range(6):
            if (i, j) in rope:
                print(rope.index((i, j)), end="")
            else:
                print(".", end="")
        print()
    print()

# run simulation
for line in lines:
    direction, _, units = line.partition(' ')
    print(direction, units)
    for i in range(int(units)):
        # move the head
        rope[0] = move(rope[0], direction)
        #print(f"i {i} head {rope[0]}")
        # move each knot of remaining rope in order
        for k in range(1, len(rope)):
            # "head" = rope[k-1]
            # "tail" = rope[k]
            #print(f"k {k} {rope[k-1]}", end=" ")
            #print("tail start", rope[k], end=" ")
            if is_touching(rope[k-1], rope[k]):
                # do nothing
                continue
            elif is_directly_two_steps_away(rope[k], rope[k-1]):
                # move 1 step cardinally
                rope[k] = move(rope[k], direction)
            else:
                # move 1 step diagonally
                bearing = get_bearing(rope[k], rope[k-1])
                rope[k] = move(rope[k], bearing)
            #print("tail end", rope[k])
            
        # remember the tail position
        visited_set.add(rope[rope_length-1])

        #print_rope()

print(visited_set)
print("visited positions: ", len(visited_set))