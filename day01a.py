maxCalories = 0

with open('input.txt') as reader:
    line = reader.readline()
    calories = int(line)
    while line != '':
        
        if line.strip() == '':
            maxCalories = max(maxCalories, calories)
            calories = 0
        else:
            calories = calories + int(line)
        line = reader.readline()

print(maxCalories)