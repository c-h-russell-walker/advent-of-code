# http://adventofcode.com/day/3

with open('input.txt') as f:
    instructions = f.read().strip()

    first_year_location = [0, 0]
    location = [0, 0]
    robo_location = [0, 0]

    first_year = {str(first_year_location): 1}
    present_registry = {str(location): 1}

    for idx, char in enumerate(instructions):

        if char == '^':
            first_year_location[1] -= 1
        elif char == 'v':
            first_year_location[1] += 1
        elif char == '<':
            first_year_location[0] -= 1
        elif char == '>':
            first_year_location[0] += 1

        if first_year.get(str(first_year_location)) and first_year.get(str(first_year_location)) >= 0:
            first_year[str(first_year_location)] += 1
        else:
            first_year[str(first_year_location)] = 1

        if idx % 2 == 0:
            if char == '^':
                robo_location[1] -= 1
            elif char == 'v':
                robo_location[1] += 1
            elif char == '<':
                robo_location[0] -= 1
            elif char == '>':
                robo_location[0] += 1

            if present_registry.get(str(robo_location)) and present_registry.get(str(robo_location)) >= 0:
                present_registry[str(robo_location)] += 1
            else:
                present_registry[str(robo_location)] = 1
        else:
            if char == '^':
                location[1] -= 1
            elif char == 'v':
                location[1] += 1
            elif char == '<':
                location[0] -= 1
            elif char == '>':
                location[0] += 1

            if present_registry.get(str(location)) and present_registry.get(str(location)) >= 0:
                present_registry[str(location)] += 1
            else:
                present_registry[str(location)] = 1

    multiple_presents = 0

    for loc, presents in present_registry.items():
        if presents:
            multiple_presents += 1

    print("At least one present: {}".format(len(first_year)))
    print("Multiple Presents: {}".format(multiple_presents))
