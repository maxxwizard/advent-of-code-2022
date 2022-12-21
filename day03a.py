def get_priority(item_type: str) -> int:
    order = ord(item_type)
    if order > ord('Z'):
        val = order - ord('a') + 1
    else:
        val = order - ord('A') + 1 + 26
    if val <= 0 or val > 52:
        raise Exception()
    return val

def split_list(a_list):
    mid = len(a_list)//2
    return a_list[:mid], a_list[mid:]

# split rucksacks in 2 halves
# turn it into 2 sets
# find the intersection
# convert common item type to priority
# return sum
with open('input.txt') as reader:
    line = reader.readline().strip()
    sum = 0
    while line != '':
        a,b = map(lambda x: set(x), split_list(line))
        common = a.intersection(b)
        print(common, end=' ')
        priority = get_priority(common.pop())
        print(priority)
        sum += priority
        line = reader.readline().strip()
    print(sum)