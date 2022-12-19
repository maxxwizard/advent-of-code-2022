from queue import PriorityQueue
# priority queue of elves' calories
q = PriorityQueue()

with open('input.txt') as reader:
    line = reader.readline()
    calories = int(line)
    while line != '':
        
        if line.strip() == '':
            #print('BLANK')
            q.put((-calories, calories))
            calories = 0
        else:
            calories = calories + int(line)
            #print(line, end='')
        line = reader.readline()

for x in range(3):
    print(q.get())