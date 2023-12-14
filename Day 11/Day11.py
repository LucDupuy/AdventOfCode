import numpy as np


def add_stuff(universe):
    expanded = []
    for line in universe:
        if "#" not in line:
            expanded.append([char for char in line])
        expanded.append([char for char in line])

    return expanded


def number_the_galaxies(universe):
    galaxy_locations = []
    total = 0
    num = 0
    for row_idx, line in enumerate(universe):
        for col_idx, char in enumerate(line):
            if char == "#":
                galaxy_locations.append((row_idx, col_idx))
                universe[row_idx][col_idx] = num
                num += 1
                total+= 1
    return universe, total, galaxy_locations


file = open("input.txt", 'r')
list = file.read().splitlines()
expanded_universe = add_stuff(list)
expanded_universe = add_stuff(np.transpose(expanded_universe))
expanded_universe = np.transpose(expanded_universe)
expanded_universe, num_galaxies, galaxy_locations = number_the_galaxies(expanded_universe)
expanded_universe = expanded_universe.tolist()

distances = []

for i in range(0, num_galaxies):
    for j in range(i+1, num_galaxies):
        start_row, start_col, end_row, end_col = galaxy_locations[i][0], galaxy_locations[i][1], galaxy_locations[j][0], galaxy_locations[j][1]
        distances.append(abs((start_row - end_row)) + abs((start_col-end_col)))
        

print(sum(distances))
