# http://adventofcode.com/day/1

with open('input.txt') as f:
    day_1_input = f.read().strip()

    floor = 0
    position = None
    for idx, char in enumerate(day_1_input):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        if not position and floor == -1:
            position = idx + 1

    print("Floor: {}".format(floor))
    print("Position: {}".format(position))