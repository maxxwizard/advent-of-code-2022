# sliding window of 4
# output end if counter dictionary has 4 unique chars

from collections import Counter


start = 0; end = 0; windowSize = 4
chars = Counter()
line = ''
with open('input.txt') as reader:
    line = reader.readline().strip()

while True:
    c = line[end]
    print(c)
    if not c:
        raise Exception("this should not be possible with valid input")
    
    # add 1 to this char's count
    chars.update(c)

    # shrink window
    while end-start >= windowSize:
        d = line[start]
        chars.subtract(d)
        if chars[d] == 0:
            del chars[d]
        start += 1

    print(chars)

    # check if 4 unique chars in window
    if end-start+1 == windowSize and len(chars) == windowSize:
        print(end+1, "characters must be processed")
        exit()
    
    # expand window
    end += 1
