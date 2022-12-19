def isRock(hand: str):
    return hand == 'A'

def isPaper(hand: str):
    return hand == 'B'

def isScissors(hand: str):
    return hand == 'C'

def value(yourHand: str):
    match yourHand:
        case 'A':
            return 1
        case 'B':
            return 2
        case 'C':
            return 3
    raise ValueError(f"invalid hand {yourHand}")

def getYourHand(instruction: str, theirHand: str) -> str:
    match instruction:
        case 'X': # you should lose
            if isRock(theirHand):
                return 'C'
            if isPaper(theirHand):
                return 'A'
            if isScissors(theirHand):
                return 'B'
        case 'Y': # you should draw
            return theirHand
        case 'Z': # you should win
            if isRock(theirHand):
                return 'B'
            if isPaper(theirHand):
                return 'C'
            if isScissors(theirHand):
                return 'A'
    raise Exception('invalid instruction')

def points(yourHand, theirHand):
    match yourHand: # look for wins
        case 'A':
            if theirHand == 'C':
                return 6 # rock beats scissors
            if theirHand == 'A':
                return 3 # draw
        case 'B':
            if theirHand == 'A':
                return 6 # paper beats rock
            if theirHand == 'B':
                return 3 # draw
        case 'C':
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
        instruction = parts[2].strip()
        yourHand = getYourHand(instruction, theirHand)
        score += value(yourHand)
        score += points(yourHand, theirHand)
        line = reader.readline()
    print(score)