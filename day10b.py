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

def printScanline():
    global X, cycle
    if (cycle % 40) in (X-1, X, X+1):
        print("#", end="")
    else:
        print(".", end="")

cycle = 0
while i < len(lines):
    if cycle % 40 == 0:
        print()
    printScanline()
    if pendingOp:
        pendingOp = False
        X += pendingParam
    else:
        op, param = getNextInstruction()
        # noop does nothing
        if op == "addx":
            pendingParam = int(param)
            pendingOp = True
    cycle += 1
