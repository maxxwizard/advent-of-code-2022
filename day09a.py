# read in motions
with open('input.txt') as reader:
    lines = reader.readlines()
lines = list(map(lambda l: l.strip(), lines))

# use a set to store visited coordinates
visited_set = set()

# head and tail start at origin
head = (0, 0); tail = (0, 0)
visited_set.add(tail)

# same coordinates or adjacent
def is_touching() -> bool:
    global head, tail
    if head[0] == tail[0] and head[1] == tail[1]:
        return True
    elif move(head, 'U') == tail:
        return True
    elif move(head, 'D') == tail:
        return True
    elif move(head, 'L') == tail:
        return True
    elif move(head, 'R') == tail:
        return True
    elif move(head, 'NE') == tail:
        return True
    elif move(head, 'NW') == tail:
        return True
    elif move(head, 'SE') == tail:
        return True
    elif move(head, 'SW') == tail:
        return True
    return False

def is_directly_two_steps_away() -> bool:
    global head, tail
    if head[0] == tail[0]:
        return (abs(head[1] - tail[1]) == 2)
    if head[1] == tail[1]:
        return (abs(head[0] - tail[0]) == 2)
    
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

def get_ordinal_direction(src, dst) -> str:
    if dst[0] > src[0] and dst[1] > src[1]:
        return 'NE'
    if dst[0] > src[0] and dst[1] < src[1]:
        return 'SE'
    if dst[0] < src[0] and dst[1] > src[1]:
        return 'NW'
    if dst[0] < src[0] and dst[1] < src[1]:
        return 'SW'
    raise ValueError()

# run simulation
for line in lines:
    direction, _, units = line.partition(' ')
    print(direction, units)
    for i in range(int(units)):
        # move the head
        head = move(head, direction)
        # move the tail in response
        if is_touching():
            # do nothing
            continue
        elif is_directly_two_steps_away():
            # move 1 step cardinally
            tail = move(tail, direction)
        else:
            # move 1 step diagonally
            bearing = get_ordinal_direction(tail, head)
            tail = move(tail, bearing)
        # remember the tail position
        visited_set.add(tail)

print(visited_set)
print("visited positions: ", len(visited_set))