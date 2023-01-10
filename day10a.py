X = 1
pendingOp = False
pendingParam = 0
sum = 0

with open('input.txt') as reader:
    lines = reader.readlines()
lines = list(map(lambda l: l.strip(), lines))
i = 0

def getNextInstruction():
    global i, lines
    line = lines[i]
    i += 1
    op, _, param = line.partition(" ")
    return (op, param)

for cycle in range(1, 221):
    if (cycle - 20) % 40 == 0:
        strength = cycle * X
        sum += strength
        print(f"cycle {cycle}, X {X}, strength {strength}, sum {sum}")
    if pendingOp:
        pendingOp = False
        X += pendingParam
    else:
        op, param = getNextInstruction()
        # noop does nothing
        if op == "addx":
            pendingParam = int(param)
            pendingOp = True

print("finito")