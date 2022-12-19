def value(yourHand: str):
    match yourHand:
        case 'X':
            return 1
        case 'Y':
            return 2
        case 'Z':
            return 3
    print(f"yours {yourHand}")
    raise ValueError()

def points(yourHand, theirHand):
    match yourHand: # look for wins
        case 'X':
            if theirHand == 'C':
                return 6 # rock beats scissors
            if theirHand == 'A':
                return 3 # draw
        case 'Y':
            if theirHand == 'A':
                return 6 # paper beats rock
            if theirHand == 'B':
                return 3 # draw
        case 'Z':
            if theirHand == 'B':
                return 6 # scissors beats paper
            if theirHand == 'C':
                return 3 # draw
    return 0 # you lost

with open('input.txt') as reader:
    line = reader.readline()
    score = 0
    while line != '':
        parts = line.partition(' ')
        theirHand = parts[0].strip()
        yourHand = parts[2].strip()
        score += value(yourHand)
        score += points(yourHand, theirHand)
        line = reader.readline()
    print(score)