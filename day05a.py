# there are 9 stacks of max height 8
max_height = 8
num_stacks = 9

def create_stacks(matrix: list[str]):
    # init stacks
    stacks = []
    for i in range(num_stacks):
        stacks.append([])

    # read from bottom to top and create the stacks
    for m in reversed(matrix):
        #print(m)
        for i in range(num_stacks):
            stack = stacks[i]
            offset = i*4 + 1
            #print(offset, end=' ')
            letter = m[offset]
            #print(letter)
            if letter != ' ':
                stack.append(letter)
        #print()
    
    return stacks

def process_instruction(stacks: list[list[str]], instruction: str):
    #print(instruction)
    tokens = instruction.split(' ')
    num = int(tokens[1])
    src = int(tokens[3])-1
    dst = int(tokens[5])-1
    #print(num, src, dst)
    for i in range(num):
        #print(f"moving {src} to {dst}")
        stacks[dst].append(stacks[src].pop())

# read in "matrix"
lines = list[str]
with open('input.txt') as reader:
    lines = reader.readlines()

# create stacks in memory
stacks: list[list[str]] = create_stacks(lines[0:max_height])

# process instructions
for line in lines[max_height+2:]:
    process_instruction(stacks, line.strip())

# print out top of each stack
for s in stacks:
    print(s.pop())