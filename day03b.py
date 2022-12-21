def get_priority(item_type: str) -> int:
    order = ord(item_type)
    if order > ord('Z'):
        val = order - ord('a') + 1
    else:
        val = order - ord('A') + 1 + 26
    if val <= 0 or val > 52:
        raise Exception()
    return val

# split rucksacks in 2 halves
# turn it into 2 sets
# find the intersection
# convert common item type to priority
# return sum
with open('input.txt') as reader:
    sum = 0
    while reader:
        a = set(reader.readline().strip())
        b = set(reader.readline().strip())
        c = set(reader.readline().strip())
        if len(a) == 0:
            break # done with file
        common = a.intersection(b).intersection(c)
        print(common, end=' ')
        priority = get_priority(common.pop())
        print(priority)
        sum += priority
    print(sum)