def to_int(val: str):
    try:
        return int(val)
    except:
        return 0

def overlaps(range1: str, range2: str):
    l1, _, h1 = map(lambda x: to_int(x), range1.partition('-'))
    l2, _, h2 = map(lambda x: to_int(x), range2.partition('-'))
    if l1 >= l2 and l1 <= h2:
        return True
    if l2 >= l1 and l2 <= h1:
        return True
    if h1 >= l2 and h1 <= h2:
        return True
    if h2 >= l1 and h2 <= h1:
        return True
    return False

with open('input.txt') as reader:
    count = 0
    while reader:
        line = reader.readline().strip()
        if line == '':
            break # EOF
        range1, _, range2 = line.partition(',')
        print(range1, range2)
        if overlaps(range1, range2):
            count += 1
    print(count)